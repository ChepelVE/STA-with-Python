import pytest

from hw1 import merge_sorted_files


@pytest.mark.parametrize(
    "files, expected", [(["file1.txt", "file2.txt"], [1, 2, 3, 4, 5, 6]),
                        (["file1.txt", "file2.txt", "file3.txt"], [1, 2, 3, 4, 5, 6, 8, 9, 15])]
)
def test_hw1(files, expected):
    assert list(merge_sorted_files(files)) == expected
