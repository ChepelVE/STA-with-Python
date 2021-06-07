import pytest

from task2 import TableData


@pytest.fixture
def table_data():
    return TableData(database_name='example.sqlite', table_name='presidents')


def test_task2_len(table_data):
    assert len(table_data) == 3


def test_task2_yeltsin(table_data):
    assert table_data['Yeltsin'] == ('Yeltsin', 999, 'Russia')


def test_task2_yeltsin2(table_data):
    assert ('Yeltsin' in table_data) == True
