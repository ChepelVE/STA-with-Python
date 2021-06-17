from requests import get
from bs4 import BeautifulSoup as bs
import json
from datetime import date
import xml.etree.ElementTree as ET

class Company:
    code, pe, price, week_low, week_high = None, None, None, None, None

    def __init__(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        code_el = soup.find('span', class_='price-section__category').findChild()
        price_el = soup.find('span', class_='price-section__current-value')
        week_low_el = soup.find('div', class_='snapshot__data-item snapshot__data-item--small')
        week_high_el = \
            soup.find('div',
                      class_='snapshot__data-item snapshot__data-item--small snapshot__data-item--right')
        if code_el:
            self.code = code_el.getText()[2:]
        if price_el:
            self.price = price_el.getText()
        if week_low_el:
            self.week_low = week_low_el.getText().split(" ")[0].strip()[:-3].strip()
        if week_high_el:
            self.week_high= week_high_el.getText().split(" ")[0].strip()[:-3].strip()

    def __str__(self):
        return f'Code={self.code}, Price={self.price}, P/E={self.pe}, Week Low={self.week_low}, ' \
               f'Week high={self.week_high}'
        #  return f'Code={self.code}, Price={self.price}'

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

def get_next_sibling_by_number(element, order: int):
    sibling_el = element
    while order != 0:
        sibling_el = sibling_el.find_next_sibling()
        order -= 1
    return sibling_el


def get_current_dollar_exchange_rate():
    current_date = date.today().strftime("%d/%m/%Y")
    url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={current_date}'
    xml = get(url).text
    xml_tree = bs(xml, "lxml").html.body.valcurs
    usd_rate = xml_tree.find("valute", {"id": "R01235"}).value.text
    return usd_rate

get_current_dollar_exchange_rate()