import pytest

from bad import create_country_make_dict as bad_dict
from good import create_country_make_dict as good_dict

REQUEST_URL = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers?format=json"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_dict_length(dict_func):
    dict_length = len(dict_func(REQUEST_URL))
    assert dict_length == 79, f"Expected length to be 79, but got {dict_length} instead"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_us_length(dict_func):
    dict_func(REQUEST_URL)
    us_length = len(dict_func(REQUEST_URL)["UNITED STATES (USA)"])
    assert us_length == 14869, f"Expected length for UNITED STATES (USA) to be 14869, but got {us_length} instead"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_mexico_length(dict_func):
    dict_func(REQUEST_URL)
    mexico_length = len(dict_func(REQUEST_URL)["MEXICO"])
    assert mexico_length == 188, f"Expected length for MEXICO to be 188, but got {mexico_length} instead"


@pytest.mark.parametrize("dict_func", [bad_dict, good_dict])
def test_germany_length(dict_func):
    dict_func(REQUEST_URL)
    germany_length = len(dict_func(REQUEST_URL)["GERMANY"])
    assert germany_length == 99, f"Expected length for GERMANY to be 99, but got {germany_length} instead"
