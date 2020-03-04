"""
Given a list of numbers, compute the simple moving average for window length 20.
Output the simple moving average to a new list.

Conceptually very similar to the simple cumulative sum case.
"""

import pandas as pd
from numba import jit
import numpy as np
from pretty_cool_profiler import time_this, timed_report
from typing import List

def random_numeric_list(n):
    return np.random.random(n)


@time_this
def slow_moving_average(values: List[float], m: int=20):
    """
    This is O(nm) time, because it re-computes the sum at every step
    1 + 2 + 3 + 4 + ... / m
    2 + 3 + 4 + 5 + ... / m
    3 + 4 + 5 + 6 + ... / m
    4 + 5 + 6 + 7 + ... / m
    and so on ...
    Leading to approx (m-1) * n individual additions.
    """

    # Initial values
    moving_average = [None] * (m-1)

    for i in range(m-1, len(values)):
        the_average = np.mean(values[(i-m+1):i+1])
        moving_average.append(the_average)

    return moving_average

@time_this
def fast_moving_average(values: List[float], m: int=20):
    """
    This is O(n) time, because it keeps track of the intermediate sum.
    Leading to approx 2n individual additions.
    """

    # Initial values
    moving_average = [None] * (m-1)
    accumulator = sum(values[:m])
    moving_average.append(accumulator / m)

    for i in range(m, len(values)):
        accumulator -= values[i-m]
        accumulator += values[i]
        moving_average.append(accumulator / m)

    return moving_average

@time_this
def pandas_moving_average(values: pd.Series, m: int=20):
    """
    The pandas implementation is efficient at O(n) time.
    """
    return values.rolling(m).mean()

# @time_this
# def slow_cumulative_sum(values: List[float], m: int=20):
#   """
#   This is O(nm) time, because it re-computes the sum at every step
#   1 + 2 + 3 + 4
#   2 + 3 + 4 + 5
#   3 + 4 + 5 + 6
#   4 + 5 + 6 + 7
#   and so on ...
#   Leading to (m-1) * n individual additions.
#   """

#   moving_average = [None] * (m-1)

#   for i in range(m, len(values)):
#       assert len(values[(i+1-m):i+1]) == m
#       the_average = sum(values[(i+1-m):i+1]) / m
#       cumulative_sum.append(the_average)

#   return moving_average


if __name__ == '__main__':

    # values = random_numeric_list(101)
    # slow_results = slow_moving_average(values)
    # fast_results = fast_moving_average(values)
    # pandas_results = pandas_moving_average(values)

    # print(pd.DataFrame([slow_results, fast_results, pandas_results]).values.T)

    with timed_report():
        for i in range(5):
            values = random_numeric_list(10**(i+2))
            result = slow_moving_average(values)

        for i in range(6):
            values = random_numeric_list(10**(i+2))
            result = fast_moving_average(values)

        for i in range(7):
            values = random_numeric_list(10**(i+2))
            result = pandas_moving_average(pd.Series(values))
