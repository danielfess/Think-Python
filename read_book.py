import string

def make_word_dict():
    file = open('words.txt')
    d = dict()
    for line in file:
        word = line.strip()
        d[word] = None
    return d

word_reference = make_word_dict()

def word_histogram(book):
    """Reads the open text file 'book' and returns a
    dictionary with the keys being the words
    appearing in 'book', with values their frequencies.
    Also outputs a list of the words sorted by
    frequency, the number of words in 'book', as well
    as any words in the book not in word_reference.

    book: text file

    output: dict, int
    """

    word_hist = dict()
    word_count = 0
    header = 1
    new_words = list()
    for line in book:
        if header == 1:
            if line[:9] == '*** START':
                header = 0
                i=0
            continue
        if header == 0:
            if line[:7] == '*** END':
                break
        line = line.strip()
        line = line.replace('—',' ')
        table = line.maketrans(line,line,string.punctuation + '“”‘£’')
        line = line.translate(table)
        line = line.lower()
        line_list = line.split(' ')
        for word in line_list:
            if word != '':
                word_hist[word] = word_hist.setdefault(word,0) + 1
                word_count += 1
                if word not in word_reference and word not in new_words:
                    new_words.append(word)
        sorted_hist = sorted(word_hist, key=word_hist.get, reverse=True)
    return sorted_hist, word_hist, word_count, new_words

sherlock_text = open('sherlock_holmes.txt', encoding = 'utf8')
sherlock_sorted, sherlock_hist, sherlock_count, sherlock_new = word_histogram(sherlock_text)
#print(sherlock_count)
#print(len(sherlock_sorted))
#print(sherlock_sorted[0:20])
#print(sherlock_new)

pride_text = open('pride_and_prejudice.txt', encoding = 'utf8')
pride_sorted, pride_hist, pride_count, pride_new = word_histogram(pride_text)
#print(pride_count)
#print(len(pride_hist))
#print(pride_sorted[0:20])
#print(pride_new)

alice_text = open('alice_in_wonderland.txt', encoding = 'utf8')
alice_sorted, alice_hist, alice_count, alice_new = word_histogram(alice_text)
#print(alice_count)
#print(len(alice_hist))
#print(alice_sorted[0:20])
#print(alice_new)
