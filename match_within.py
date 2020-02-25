"""
Given two lists of words, return the elements from the first list that are in 
the second list.
"""
import random
import string
import pandas as pd
from pretty_cool_profiler import time_this, timed_report

def random_words(n):
	big_list = random.choices(string.ascii_uppercase + string.digits, k=n*7)
	return [''.join(big_list[i:(i+7)]) for i in range(n)]

@time_this
def slow_match_within(first_list, second_list):
	"""
	This algorithm is O(nm) for n unique words in the first list and m total 
	words in the second list
	"""

	# Our output data structure will be a list of tuples
	words = list()

	# Get the unique words
	unique_words = set(first_list)

	for word in unique_words:
		# This operation is O(m)
		if word in second_list:
			words.append(word)

	return words

@time_this
def fast_match_within(first_list, second_list):
	"""
	This algorithm is O(n + m) for n unique words in the first list and m words 
	in the second list
	"""

	# Our output data structure will be a list of tuples
	words = list()

	# Get the unique words
	unique_words = set(first_list)
	second_list_as_set = set(second_list)

	for word in unique_words:
		# This operation is O(1)
		if word in second_list_as_set:
			words.append(word)

	return words

@time_this
def fast_intersection(first_list, second_list):
	"""
	This algorithm is O(n + m) for n words in the first 
	list and m words in the second list

	This problem boils down to nothing more than a set intersection, so you can 
	use Python's built-in data structures to turn it into a one-liner
	"""
	return set(first_list) & set(second_list)


@time_this
def pandas_index_intersection(first_list, second_list):
	"""
	This algorithm is O(n + m) for n words in the first 
	list and m words in the second list

	I did this to settle an argument about whether or not pandas indexes are 
	set-like. They indeed are, meaning they have O(1) lookup time.
	"""
	first_list_as_set = set(first_list)
	series = pd.Series([None]*len(first_list_as_set), index=first_list_as_set)

	second_list_as_set = set(second_list)
	words = list()

	for word in second_list_as_set:
		if word in series.index:
			words.append(word)

	return word

if __name__ == '__main__':

	# print(slow_count_within(['A', 'A', 'C', 'B'], ['A', 'B']))
	# print(fast_count_within(['A', 'A', 'C', 'B'], ['A', 'B']))

	with timed_report():
		for i in range(4):
			first_list = random_words(10**(i+1))
			second_list = random_words(10**(i+1))
			slow_match_within(first_list, second_list)

		print()
		for i in range(6):
			first_list = random_words(10**(i+1))
			second_list = random_words(10**(i+1))
			fast_match_within(first_list, second_list)

		print()
		for i in range(6):
			first_list = random_words(10**(i+1))
			second_list = random_words(10**(i+1))
			fast_intersection(first_list, second_list)

		print()
		for i in range(6):
			first_list = random_words(10**(i+1))
			second_list = random_words(10**(i+1))
			pandas_index_intersection(first_list, second_list)

