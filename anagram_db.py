import anagram_sets
import shelve

def store_anagrams():
	"""Stores dictionary of anagrams in permanent storage
	as a shelf.
	"""

	anagram_dict = anagram_sets.make_anagram_dict()
	anagram_shelf = shelve.open('anagram_shelf','c')
	for key, anagrams in anagram_dict.items():
		anagram_shelf[key] = anagrams

def read_anagrams(word):
	"""Given a string of letters 'word', returns all anagrams
	of this string.
	"""

	shelf = shelve.open('anagram_shelf')
	string = ''.join(sorted(word))
	return shelf[string]


#store_anagrams()
print(read_anagrams('bin'))
print(read_anagrams('arch'))