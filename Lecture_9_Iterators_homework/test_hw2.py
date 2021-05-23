import pytest

from hw2 import suppressor, suppressor_gen


def test_suppressor():
    raised = False
    lst = [1, 2, 3]
    try:
        with suppressor(IndexError):
            lst[5]
    except IndexError:
        raised = True
    assert raised is False


def test_suppressor_gen():
    raised = False
    lst = [1, 2, 3]
    try:
        with suppressor_gen(IndexError):
            lst[5]
    except IndexError:
        raised = True
    assert raised is False
