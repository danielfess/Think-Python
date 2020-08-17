#Markov analysis

import random

def text_to_list(book):
    """Reads the open text file 'book' and returns its words
    in a list.  Retains punctuation.

    book: .txt file

    output: list
    """

    word_list = list()
    header = 1
    for line in book:
        if header == 1:
            if line[:9] == '*** START':
                header = 0
            continue
        if header == 0:
            if line[:7] == '*** END':
                break
        line = line.strip()
        line = line.replace('—',' ')
        line_list_initial = line.split(' ')
        line_list_final = []
        for entry in line_list_initial:
        	if entry != '':
        		line_list_final.append(entry)
        word_list += line_list_final
    return word_list

def markov(text,prefix_len, text2 = False):
	"""Given a text, returns a dictionary where the keys are
	tuples of strings of length 'prefix_len' and the values are
	all suffixes in 'text' which follow such a prefix.  The
	frequency of each prefix-suffix pair is also recorded.
	'text2' is an optional second text.

	text: file in .txt format
	prefix: int > 0
	text2: .txt file

	output: dict, with tuples for keys and dicts for values
	"""

	book = open(text,encoding = 'utf8')
	word_list = text_to_list(book)
	if text2 != False:
		book2 = open(text2,encoding = 'utf8')
		word_list += text_to_list(book2)
	markov_dict = dict()
	for i in range(len(word_list)-prefix_len):
		prefix = tuple(word_list[i:i + prefix_len])
		suffix = word_list[i + prefix_len]
		if prefix not in markov_dict:
			markov_dict[prefix] = {suffix : 1}
		else:
			markov_dict[prefix][suffix] = markov_dict[prefix].setdefault(suffix,0) + 1
	return markov_dict

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

def random_text(text, prefix_len, sentences, freq = False, text2 = False):
	"""Produces random sentences from a text using output from
	the function markov.  'freq' is a bool which enables the
	random choices to be made according to the frequency of a
	prefix-suffix pair.  'prefix_len' is the same as for the
	function markov.  'sentences' is number of sentences.
	'text2' is an optional second text.

	markov_dict: dict
	sentence: int > 0
	freq: bool
	text2: .txt file

	output: string
	"""

	book = open(text, encoding = 'utf8')
	num_sentences = 0
	text_list = text_to_list(book)
	if text2 != False:
		book2 = open(text2, encoding = 'utf8')
		text_list += text_to_list(book2)
	starting_words = dict()
	for word in text_list:
		if word[0].isupper() or (len(word) > 1 and word[1].isupper()):
			starting_words[word] = starting_words.setdefault(word,0) + 1
	if freq == False:
		start = random.choice(list(starting_words))
	else:
		start = choose_from_hist2(starting_words)
	sample_text = [start]
	if start[-1] == '.':
		num_sentences += 1
		if num_sentences == sentences:
			print(' '.join(sample_text))
			return ' '.join(sample_text)
	for i in range(1,prefix_len + 1):
		d = markov(text,i,text2)
		prefix = tuple(sample_text)
		if freq == False:
			suffix = random.choice(list(d[prefix]))
		else:
			suffix = choose_from_hist2(d[prefix])
		sample_text.append(suffix)
		if suffix[-1] == '.':
			num_sentences += 1
			if num_sentences == sentences:
				return sample_text
	while True:
		prefix = tuple(sample_text[-prefix_len:])
		if freq == False:
			suffix = random.choice(list(d[prefix]))
		else:
			suffix = choose_from_hist2(d[prefix])
		sample_text.append(suffix)
		if suffix[-1] == '.':
			num_sentences += 1
			if num_sentences == sentences:
				break
	sample_text = ' '.join(sample_text)
	print(sample_text)
	return sample_text

rtext = random_text('sherlock_holmes.txt',3,7,True, 'pride_and_prejudice.txt')