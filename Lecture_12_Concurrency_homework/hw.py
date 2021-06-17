import aiohttp
import asyncio
import json
import requests
from bs4 import BeautifulSoup as bs
from datetime import date

company_codes = []
companies = []
dollar_exchange_rate = None


class Company:
    code, pe, price, growth, potential_profit, name = None, None, None, None, None, None

    def __init__(self, html: str, growth):
        week_low, week_high, price_un_dollars = None, None, None
        soup = bs(html, "html.parser")
        code_el = soup.find('span', class_='price-section__category').findChild()
        name_el = soup.find('span', class_='price-section__label')
        price_el = soup.find('span', class_='price-section__current-value')
        week_low_el = soup.find('div', class_='snapshot__data-item snapshot__data-item--small')
        week_high_el = soup.find('div',
                                 class_='snapshot__data-item snapshot__data-item--small snapshot__data-item--right')
        pe_el = get_next_sibling_by_number(soup.find('div', class_='snapshot__data-item'), 7)
        if name_el: self.name = name_el.getText()
        if code_el: self.code = code_el.getText()[2:]
        if price_el: price_un_dollars = float(price_el.getText().replace(',', ''))
        if week_low_el: week_low = float(week_low_el.getText().split(" ")[0].strip()[:-3].strip().replace(',', ''))
        if week_high_el: week_high = float(week_high_el.getText().split(" ")[0].strip()[:-3].strip().replace(',', ''))
        if pe_el:
            self.pe = pe_el.getText()
            if "P/E Ratio" in self.pe:  # у некоторых компаний нет такого параметра, но дркгой элемент находится
                # https://markets.businessinsider.com/stocks/alle-stock
                self.pe = float(self.pe.strip()[:-9].strip().replace(',', ''))
            else:
                self.pe = None
        self.growth = float(growth)
        if week_low and week_high: self.calculate_potential_profit(week_low, week_high)
        if price_un_dollars: self.calculate_price_in_rubles(price_un_dollars)

    def to_base_dict(self):
        return {"name": self.name, "code": self.code}

    def to_dict_with_pe(self):
        dict_with_pe = self.to_base_dict()
        dict_with_pe.update({"P/E": self.pe})
        return dict_with_pe

    def to_dict_with_price(self):
        dict_with_price = self.to_base_dict()
        dict_with_price.update({"price": self.price})
        return dict_with_price

    def to_dict_with_growth(self):
        dict_with_growth = self.to_base_dict()
        dict_with_growth.update({"growth": self.growth})
        return dict_with_growth

    def to_dict_with_profit(self):
        dict_with_profit = self.to_base_dict()
        dict_with_profit.update({"potential profit": self.potential_profit})
        return dict_with_profit

    def calculate_price_in_rubles(self, price_in_dollars):
        self.price = price_in_dollars * dollar_exchange_rate

    def calculate_potential_profit(self, week_low, week_high):
        self.potential_profit = dollar_exchange_rate * (week_high - week_low)


async def get_company_details(session, url, growth):
    async with session.get(url) as resp:
        html = await resp.text()
        new_company = Company(html, growth)
        print(new_company.to_base_dict())
        companies.append(new_company)


async def get_links_and_growth_from_page(session, url):
    async with session.get(url) as resp:
        tasks = []
        html = await resp.text()
        soup = bs(html, "html.parser")
        for tr in soup.tbody.find_all('tr'):
            growth = get_next_sibling_by_number(tr.td, 7).find('br').find_next_sibling().getText()[:-1]
            company_link = tr.td.a.get('href')
            comp_url = f'https://markets.businessinsider.com{company_link}'
            print(comp_url)
            tasks.append(asyncio.ensure_future(get_company_details(session, comp_url, growth)))
            await asyncio.gather(*tasks)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []

        for page in range(1, 11):
            sp_url = f'https://markets.businessinsider.com/index/components/s&p_500?p={page}'
            tasks.append(asyncio.ensure_future(get_links_and_growth_from_page(session, sp_url)))
            await asyncio.gather(*tasks)


def get_next_sibling_by_number(element, order: int):
    sibling_el = element
    while order != 0:
        sibling_el = sibling_el.find_next_sibling()
        order -= 1
    return sibling_el


def get_current_dollar_exchange_rate():
    current_date = date.today().strftime("%d/%m/%Y")
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}'
    xml = requests.get(url).text
    xml_tree = bs(xml, "lxml").html.body.valcurs
    usd_rate = xml_tree.find("valute", {"id": "R01235"}).value.text
    return float(usd_rate.replace(',', '.'))


def none_type_float_key_mapper(x):
    if not x:
        return float(0)
    return x


if __name__ == '__main__':
    dollar_exchange_rate = get_current_dollar_exchange_rate()
    asyncio.get_event_loop().run_until_complete(main())
    most_expensive_companies = sorted(companies, key=lambda x:  none_type_float_key_mapper(x.price), reverse=True)
    companies_with_lowest_pe = sorted(companies, key=lambda x: none_type_float_key_mapper(x.pe))
    companies_with_highest_growth = sorted(companies, key=lambda x:  none_type_float_key_mapper(x.growth), reverse=True)
    companies_with_highest_potential_profit = \
        sorted(companies, key=lambda x:  none_type_float_key_mapper(x.potential_profit), reverse=True)
    most_expensive_companies_json_array = \
        json.dumps([c.to_dict_with_price() for c in most_expensive_companies[:10]], indent=4)
    companies_with_lowest_pe_json_array = \
        json.dumps([c.to_dict_with_pe() for c in companies_with_lowest_pe[:10]], indent=4)
    companies_with_highest_growth_json_array = \
        json.dumps([c.to_dict_with_growth() for c in companies_with_highest_growth[:10]], indent=4)
    companies_with_highest_potential_profit_json_array = \
        json.dumps([c.to_dict_with_profit() for c in companies_with_highest_potential_profit[:10]], indent=4)
    with open("most_expensive_companies.txt", "w") as most_expensive_companies_file:
        most_expensive_companies_file.write(most_expensive_companies_json_array)
    with open("companies_with_highest_growth.txt", "w") as companies_with_highest_growth_file, \
            open("companies_with_highest_potential_profit.txt", "w") as companies_with_highest_potential_profit_file, \
            open("companies_with_lowest_pe.txt", "w") as companies_with_lowest_pe_file:
        companies_with_highest_growth_file.write(companies_with_highest_growth_json_array)
        companies_with_highest_potential_profit_file.write(companies_with_highest_potential_profit_json_array)
        companies_with_lowest_pe_file.write(companies_with_lowest_pe_json_array)
