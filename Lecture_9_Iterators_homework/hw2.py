"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

>>> with suppresor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class suppressor:
    def __init__(self, exception: Exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return exc_type is not None and issubclass(exc_type, self.exception)


@contextmanager
def suppressor_gen(exception: Exception):
    try:
        yield
    except exception:
        pass
