import string
import math
import matplotlib.pyplot as plt

print(' ' in string.whitespace)

def zipf_data(file):
	"""Reads a text file and fits Zipf's law to it.
	Returns the log frequency vs log rank data.

	file: .txt file

	output: list of tuples of float
	"""

	text = open(file, encoding='utf8')
	word_dict = dict()
	for line in text:
		line = line.strip()
		line = line.replace('—',' ')
		line = line.split()
		for word in line:
			word = word.strip(string.punctuation + string.whitespace)
			word_dict[word] = word_dict.setdefault(word,0) + 1
	word_dict_sorted = sorted(word_dict, key=word_dict.get, reverse=True)
	word_zipf = list()
	r = 0
	for word in word_dict_sorted:
		r += 1
		word_zipf.append((math.log(r), math.log(word_dict[word])))
	data = list(zip(*word_zipf))
	return data

def zipf_estimate(file):
	"""Given a text file, returns an estimate of Zipf's
	parameter s, and plots the log freq vs log rank data.

	file: .txt file

	output: float
	"""

	data = zipf_data(file)
	n = len(data[0])
	x2 = [t**2 for t in data[0]]
	xy = [data[0][i]*data[1][i] for i in range(n)]
	mean_x = sum(data[0])/n
	mean_x2 = sum(x2)/n
	mean_y = sum(data[1])/n
	mean_xy = sum(xy)/n
	plt.plot(data[0],data[1],'o')
	return ((mean_xy - mean_x*mean_y)/(mean_x2 - mean_x**2))

print(zipf_estimate('sherlock_holmes.txt'))
print(zipf_estimate('alice_in_wonderland.txt'))
print(zipf_estimate('pride_and_prejudice.txt'))

plt.show()