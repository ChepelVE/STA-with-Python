import pytest

from task02 import find_links_func, get_sorted_domains_from_links_func


@pytest.mark.parametrize(
    "filepath, expected", [("test_data.html", ['mail.ru', 'neerc.ifno.ru', 'stepic.org', 'www.ya.ru', 'ya.ru'])]
)
def test_from_file(filepath, expected):
    with open(filepath, "r") as data:
        html_data = ''.join(data.readlines())
    links = find_links_func(html_data)
    assert get_sorted_domains_from_links_func(links) == expected
