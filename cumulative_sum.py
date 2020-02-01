"""
Given a list of numbers, compute their cumulative sum
Output the cumulative sum to a new list
"""
import pandas as pd
from numba import jit
import numpy as np
from pretty_cool_profiler import time_this, timed_report

def random_numeric_list(n):
	return np.random.random(n)

@time_this
def slow_cumulative_sum(values):
	"""
	This is O(n^2) time, because it computes ...
	1
	1 + 2
	1 + 2 + 3
	1 + 2 + 3 + 4
	and so on ...
	Leading to n*(n-1)/2 == (n^2 - n) / 2 individual additions, which is O(n^2)
	"""
	cumulative_sum = []

	for i in range(len(values)):
		the_sum = sum(values[:i+1])
		cumulative_sum.append(the_sum)

	return cumulative_sum

@time_this
def slow_cumulative_sum_expanded(values):
	"""
	Same as the above, O(n^2), but exposes the hidden complexity of sum()
	"""
	cumulative_sum = []

	for i in range(len(values)):

		accumulator = 0
		for j in range(i+1):
			accumulator += values[j]

		cumulative_sum.append(accumulator)

	return cumulative_sum

@time_this
def fast_cumulative_sum(values):
	"""
	This is O(n) time, because it does n additions for n values
	"""
	cumulative_sum = []
	accumulator = 0

	for value in values:
		accumulator += value
		cumulative_sum.append(accumulator)

	return cumulative_sum


@time_this
def pandas_fast_cumulative_sum(values):
	"""
	This is O(n) and optimized with C code

	Assumes values is a pandas Series object
	"""
	return values.cumsum()


@jit(nopython=True)
def raw_fast_cumulative_sum(values):
	"""
	This is O(n) time, because it does n additions for n values
	"""
	cumulative_sum = np.zeros(values.shape[0])
	accumulator = 0

	for index, value in enumerate(values):
		accumulator += value
		cumulative_sum[index] = accumulator

	return cumulative_sum


@time_this
def np_fast_cumulative_sum(values):
	return values.cumsum()


if __name__ == '__main__':
	# Get numba to run the jit optimization before testing.
	raw_fast_cumulative_sum(random_numeric_list(1000))
	
	@time_this
	def jit_fast_cumulative_sum(values):
		return raw_faster_cumulative_sum(values)

	with timed_report():
		for i in range(4):
			values = random_numeric_list(10**(i+1))
			slow_cumulative_sum(values)

		for i in range(4):
			values = random_numeric_list(10**(i+1))
			slow_cumulative_sum_expanded(values)

		for i in range(8):
			values = random_numeric_list(10**(i+1))
			fast_cumulative_sum(values)

		for i in range(8):
			values = random_numeric_list(10**(i+1))
			pandas_fast_cumulative_sum(pd.Series(values))
		
		for i in range(8):
			values = random_numeric_list(10**(i+1))
			jit_fast_cumulative_sum(values)

		for i in range(8):
			values = random_numeric_list(10**(i+1))
			np_fast_cumulative_sum(values)

