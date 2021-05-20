"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

>>> list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]

Add tests for this function.
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list) -> Iterator:
    lst = []

    for file_path in file_list:
        with open(file_path) as file_data:
            for line in file_data:
                lst.append(line.strip('\n'))

    return sorted(lst)



