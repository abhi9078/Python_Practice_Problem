import pytest


def my_func(x):
    return x + 1


def test_my_func():
    assert my_func(3) == 4
