"""Algorithm that chooses a word randomly from a book
based on frequency of words.  Algorithm works by
counting words by cumulative frequency, choosing a
random integer from 1 to len(book) and using
cumulative frequencies to find which word this
corresponds to."""

import random
from read_book import word_histogram

def bisection_search(item,t):
	"""Given a sorted list t of distinct entries, finds
	the index i such that t[i-1] < item <= t[i].
	Works by bisection search.

	Note: If item <= t[0], returns 0.  If item > t[-1],
	returns len(t).

	item: sortable entry
	t: sorted list

	output: index (int)
	"""

	bisect = len(t)//2

	if len(t) == 1:
		if item <= t[0]:
			return 0
		else:
			return 1

	if t[bisect] == item:
		index = bisect
	elif t[bisect] > item:
		d = t[:bisect]
		index = bisection_search(item,d)
	else:
		d = t[bisect:]
		index = bisect + bisection_search(item,d)
	return index

t = [-2,1,2,5,7,11]
test = [4,7,11,12,-4,1,0,6]
for item in test:
	print(bisection_search(item,t))

def total_words(hist):
	"""Returns the sum of the values of the histogram hist"""

	return sum(hist.values())

def choose_from_hist2(hist):
	"""Given a histogram hist, chooses a key at
	random with probability proportional to
	frequency

	hist: histogram

	output: key in hist
	"""

	total = total_words(hist)
	choice = random.randint(1,total)
	words = list(hist.keys())
	cumulative_freq = []
	cumul = 0
	for word in words:
		cumul += hist[word]
		cumulative_freq.append(cumul)
	if cumulative_freq[-1] != total:
		print('Error',cumulative_freq[-1],total)
		return
	index = bisection_search(choice,cumulative_freq)
	return words[index]

hist = {'apple':7, 'banana':4, 'cherry':13, 'elephant':0, 'tiger':1}
count = {}
trials = 2000

for i in range(trials):
	choice = choose_from_hist2(hist)
	count[choice] = count.setdefault(choice,0) + 1
count_rescaled = {}
for key in count:
	count_rescaled[key] = count[key]*25/trials
print(hist)
print(count_rescaled)

sherlock_text = open('sherlock_holmes.txt', encoding = 'utf8')
sherlock_sorted, sherlock_hist, sherlock_count, sherlock_new = word_histogram(sherlock_text)

print('Some random words from Sherlock:')
for i in range(20):
	print(choose_from_hist2(sherlock_hist))

