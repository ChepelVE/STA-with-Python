"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.

For dir with two files from hw1.py:
>>> universal_file_counter(test_dir, "txt")
6
>>> universal_file_counter(test_dir, "txt", str.split)
6

"""
import os

from pathlib import Path
from typing import Callable, Optional


def files_gen(dir_path: Path, file_extension: str):
    for file in os.listdir(dir_path):
        if file.endswith(file_extension):
            yield file


def universal_file_counter(dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    files = files_gen(dir_path, file_extension)
    for file in files:
        with open(file) as file_data:
            if tokenizer is None:
                counter += len(file_data.readlines())
            else:
                for line in file_data:
                    counter += len(tokenizer(line))
    return counter


