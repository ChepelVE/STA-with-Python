from bs4 import BeautifulSoup
from requests import get
from urllib.parse import urlparse


def find_links_func(html_data: str) -> list:
    links = []
    soup = BeautifulSoup(html_data, "html.parser")
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links


def get_sorted_domains_from_links_func(links: list) -> list:
    domain_names = []
    for link in links:
        if "//" not in link and "/" not in link:
            link = f'//{link}'
        domain_name = urlparse(link).hostname
        if domain_name and domain_name not in domain_names:
            domain_names.append(domain_name)
    return sorted(domain_names)


if __name__ == '__main__':
    url = "http://google.com"
    html_data = get(url).text
    links = find_links_func(html_data)
    domain_names = get_sorted_domains_from_links_func(links)
    print(domain_names)
