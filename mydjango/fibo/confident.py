from datetime import datetime, timedelta
import pytest
from typing import Callable


@pytest.fixture
def time_tracker():
    tick = datetime.now()
    yield
    tock = datetime.now()
    print("time = > ", (tock - tick).total_seconds())


class PerformanceExceptions(Exception):
    def __init__(self, runtime: timedelta, limit: timedelta):
        self.runtime = runtime
        self.limit = limit

    def __str__(self) -> str:
        return f"Performance failed in runtime : {self.runtime.total_seconds()} , in limit time : {self.limit.total_seconds()}"


def track_performance(method: Callable, runtime_limit=timedelta(seconds=2)):
    def run_function_and_validation_run_time(*args, **kwargs):
        tick = datetime.now()
        result = method(*args, **kwargs)
        tock = datetime.now()
        time_delta = tock - tick
        print("time = > ", time_delta.total_seconds())

        if time_delta > runtime_limit:
            raise PerformanceExceptions(runtime=time_delta, limit=runtime_limit)

        return result

    return run_function_and_validation_run_time
