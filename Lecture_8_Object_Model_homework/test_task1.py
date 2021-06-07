import pytest

from task1 import KeyValueStorage


@pytest.fixture
def storage():
    return KeyValueStorage("task1.txt")


def test_task1_name(storage):
    assert storage['name'] == 'kek'


def test_task1_song(storage):
    assert storage.song == 'shadilay'


def test_task1_power(storage):
    assert storage.power == 9001
