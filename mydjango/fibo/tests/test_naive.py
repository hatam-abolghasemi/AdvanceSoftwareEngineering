from fibo.naive import fibo
from fibo.cache import fibo_cache, fibo_cached_lru
import pytest
from typing import Callable
from fibo.confident import time_tracker


@pytest.mark.parametrize("fib_func", [fibo, fibo_cache, fibo_cached_lru])
@pytest.mark.parametrize("n, expected", [(0, 0), (1, 1), (2, 1), (20, 6765)])
def test_fibo(
    time_tracker, fib_func: Callable[[int], int], n: int, expected: int
) -> None:
    res = fib_func(n)
    assert res == expected
