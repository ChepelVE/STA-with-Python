"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
import math
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    inp.sort()
    length = len(inp)
    min_count = length + 1
    curr_count = 1
    for i in range(1, length):
        if inp[i] == inp[i - 1]:
            curr_count = curr_count + 1
        else:
            if curr_count < min_count:
                min_count = curr_count
                minor_res = inp[i - 1]
            curr_count = 1
    if curr_count < min_count:
        minor_res = inp[length - 1]
    if length % 2 == 0:
        major_res = inp[length / 2]
    else:
        major_res = inp[math.ceil(length / 2)]
    return major_res, minor_res
