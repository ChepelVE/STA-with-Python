# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function named custom_range that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


def custom_range(*args):
    range_result = []
    number_of_args = len(args)
    if number_of_args == 2:
        first_letter = args[0][0]
        stop = args[1]
        for c in range(ord(first_letter), ord(stop)):
            range_result.append(chr(c))
    if number_of_args == 3:
        start = args[1]
        stop = args[2]
        for c in range(ord(start), ord(stop)):
            range_result.append(chr(c))
    if number_of_args == 4:
        start = args[1]
        stop = args[2]
        step = args[3]
        for c in range(ord(start), ord(stop), step):
            range_result.append(chr(c))
    return range_result
