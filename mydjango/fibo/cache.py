from functools import lru_cache

cache = {}


def fibo_cache(n: int) -> int:
    if n in cache:
        return cache[n]

    if n == 0 or n == 1:
        return n

    fn = fibo_cache(n - 2) + fibo_cache(n - 1)

    cache[n] = fn

    return fn


@lru_cache(maxsize=256)
def fibo_cached_lru(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibo_cache(n - 2) + fibo_cache(n - 1)
