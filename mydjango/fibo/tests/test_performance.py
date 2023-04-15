import pytest
from fibo.naive import fibo


@pytest.mark.performance
def fibo_performance():
    fibo(n=20)
