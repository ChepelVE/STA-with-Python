import pytest

from continued_fraction import cont_fraction


@pytest.mark.parametrize(
    "fraction, expected", [("239/30", "7 1 29"), ("123/10", "12 3 3"), ("123/1000", "0 8 7 1 2 5"), ("12/0", "")]
)
def test_continued_fraction(fraction, expected):
    assert cont_fraction(fraction) == expected
