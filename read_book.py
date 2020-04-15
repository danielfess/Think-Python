import string

def word_histogram(book):
    """Reads the open text file 'book' and returns a
    dictionary with the keys being the words
    appearing in 'book', with values their frequencies.
    Also outputs the number of words in 'book'

    book: text file

    output: dict, int
    """

    word_hist = dict()
    word_count = 0
    header = 1
    for line in book:
        if header == 1:
            if line[:9] == '*** START':
                header = 0
                i=0
            continue
        line = line.strip()
        table = line.maketrans(line,line,string.punctuation + '“”‘£’')
        line = line.translate(table)
        line = line.lower()
        line_list = line.split(' ')
        for word in line_list:
            if word != '':
                word_hist[word] = word_hist.setdefault(word,0) + 1
                word_count += 1
    return word_hist, word_count

sherlock_text = open('sherlock_holmes.txt', encoding = 'utf8')
sherlock_hist, sherlock_count = word_histogram(sherlock_text)
print(sherlock_count)
print(len(sherlock_hist))

pride_text = open('pride_and_prejudice.txt', encoding = 'utf8')
pride_hist, pride_count = word_histogram(pride_text)
print(pride_count)
print(len(pride_hist))

alice_text = open('alice_in_wonderland.txt', encoding = 'utf8')
alice_hist, alice_count = word_histogram(alice_text)
print(alice_count)
print(len(alice_hist))
