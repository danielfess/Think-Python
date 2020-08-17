import random

def histogram(t):
	"""Given a list t of strings, produces a
	dictionary counting how many times each
	string appears in t

	t: list of strings

	output: dict
	"""

	hist = dict()
	for entry in t:
		hist[entry] = hist.setdefault(entry,0) + 1
	return hist

def choose_from_hist(d):
	"""Given a histogram d, chooses a key at
	random with probability proportional to
	frequency

	d: histogram

	output: key in d
	"""

	total = list()
	for key in d:
		total += [key]*d[key]
	return random.choice(total)

t = ['a','a','b']
hist0 = histogram(t)

hist = {'apple':7, 'banana':4, 'cherry':13, 'elephant':0, 'tiger':1}

count = dict()
n = 1000
for i in range(n):
	choice = choose_from_hist(hist)
	count[choice] = count.setdefault(choice,0) + 1
for key in count:
	count[key] = count[key]/n
print(count)

def distribution(d):
	"""Returns the distribution for sampling from hist
	as above.

	d: histogram

	output: dict
	"""

	dist = dict()
	total = 0
	for key in d:
		total += d[key]
	for key in d:
		dist[key] = d[key]/total
	return dist

print(distribution(hist))
