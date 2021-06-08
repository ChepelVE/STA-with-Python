import os
import pytest

from hw3 import universal_file_counter


def test_hw3():
    assert universal_file_counter(os.getcwd(), "txt") == 9


def test_hw3_with_tokenaizer():
    assert universal_file_counter(os.getcwd(), "txt", str.split) == 9
