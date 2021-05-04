"""
NHTSA has a public api; the url we will be working with is 
https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json&page=1

This api endpoint returns JSON; it has the field 'Results' - a list of car manufacturers with details.
We want to create a dictionary with country as a key, and list of manufacturer names as a value, e.g:
{
    'USA': ['Tesla', 'Ford', ...],
    'Japan': ['Honda', 'Subaru', ...]
}
Use 'Mfr_Name' as a manufacturer name.
If 'Country' is empty - skip it. We should traverse through all pages of this api endpoint

bad.py has a finished implementation of this task. Your goal is to make this code better, in any
way you can think of. Put your solution in good.py
Some examples of what can be done:
- you can create your own iterator/generator to go through pages for you
- insertion of items into dictionary can be improved

Also, add more tests to the test_dict.py to check response content.
"""

from typing import Dict, List
from collections import defaultdict
import requests


class ManufacturersPages:
    def __init__(self, url_: str):
        self.url = url_
        self.page_number = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.page_number += 1
        self.page_json_content = requests.get(f"{self.url}&page={self.page_number}").json()
        if self.page_json_content["Count"]:
            return self.page_json_content
        raise StopIteration


def create_country_make_dict(url: str) -> Dict[str, List[str]]:
    country_manufacturers = defaultdict(list)
    for manufacturer_page in ManufacturersPages(url):
        for result in manufacturer_page["Results"]:
            country = result["Country"]
            if country:
                country_manufacturers[country].append(result["Mfr_Name"])
    return dict(country_manufacturers)







