"""
Given a list of words, count the number of occurrences of each word in the list.
"""
import time
import random
import string

def random_words(n):
	big_list = random.choices(string.ascii_uppercase + string.digits, k=n*7)
	return [''.join(big_list[i:(i+7)]) for i in range(n)]

import pandas as pd

runtime_table = list()
def timeit(method):
	def timed(*args, **kwargs):
		ts = time.time()
		result = method(*args, **kwargs)
		te = time.time()
		print(f'{method.__name__}')

		n = len(args[0])
		t = (te - ts) * 1000
		n_over_t = round(n / t)
		print(f'    n   = {n} values')
		print(f'    t   = {round(t, 3)} ms')
		print(f'    n/t = {n_over_t} values per ms')
		print()
		runtime_table.append({
			'function': method.__name__, 
			'n_values': n, 
			't_milliseconds': round(t, 3), 
			'values_per_ms': n_over_t,
		})
		return result
	return timed

@timeit
def slow_count_occurences(the_words):
	"""
	This algorithm is O(nm) for n characters and m unique characters
	"""

	# Our output data structure will be a list of tuples
	count_by_word = list()

	# Get a list of all unique characters using set
	unique_words = set(the_words)

	# Loop through unique characters
	for word_a in unique_words:

		# Count the occurences
		accumulator = 0
		for word_b in the_words:
			if word_a == word_b:
				accumulator += 1

		# Store the character with the count
		count_by_word.append((word_a, accumulator))

	return count_by_word

@timeit
def fast_count_occurences(the_words):
	"""
	This algorithm is O(n) for n characters
	"""

	# Our output data structure
	count_by_word = dict()

	# Loop through the string
	for word in the_words:

		# Make sure the dictionary knows about the string
		if not word in count_by_word:
			count_by_word[word] = 0

		# Incriment the counter
		count_by_word[word] += 1

	return count_by_word

@timeit
def pandas_fast_count_occurences(the_words):
	"""
	This algorithm is O(n) for n characters, assuming the input is a pandas 
	Series objects
	"""
	return the_words.value_counts()

if __name__ == '__main__':

	# the_words = ['A', 'A', 'A', 'B', 'B', 'B', 'C']
	# print(slow_count_occurences(the_words))
	# print(fast_count_occurences(the_words))
	# print(pandas_fast_count_occurences(pd.Series(the_words)))

	for i in range(4):
		the_words = random_words(10**(i+1))
		slow_count_occurences(the_words)

	print()
	for i in range(7):
		the_words = random_words(10**(i+1))
		fast_count_occurences(the_words)

	print()
	for i in range(7):
		the_words = random_words(10**(i+1))
		pandas_fast_count_occurences(pd.Series(the_words))

	print(pd.DataFrame(runtime_table))
