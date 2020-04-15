def make_word_dict():
    """Makes a dictionary with keys being the words from words.txt
    
    returns: dictionary
    """
    
    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip()
        d[word] = ''
    return d

word_dict = make_word_dict()

def read_dictionary(filename='c06d.txt'):
    """Reads from a file and builds a dictionary that maps from
    each word to a string that describes its primary pronunciation.

    Secondary pronunciations are added to the dictionary with
    a number, in parentheses, at the end of the key, so the
    key for the second pronunciation of "abdominal" is "abdominal(2)".

    filename: string
    returns: map from string to pronunciation
    """
    d = dict()
    fin = open(filename)
    for line in fin:

        # skip over the comments
        if line[0] == '#': continue

        t = line.split()
        word = t[0].lower()
        pron = ' '.join(t[1:])
        d[word] = pron

    return d

def pronounciation(word):
    """Returns a set of all pronounciations of word.
    
    word: string
    
    output: set
    """

    if word in pron_dict:
        d = [pron_dict[word]]
        i = 2
    else:
        return set([])
    while True:
        new_word = word + '(' + str(i) + ')'
        if new_word not in pron_dict:
            break
        d.append(pron_dict[new_word])
        i += 1
    return set(d)

pron_dict = read_dictionary()

print(pronounciation('abyes'))
print(pronounciation('associates'))


for word in word_dict:
    if len(word) == 5:
        word1 = word[1:]
        word2 = word[0] + word[2:]
        if word1 in word_dict and word2 in word_dict:
            pron = pronounciation(word)
            pron1 = pronounciation(word1)
            pron2 = pronounciation(word2)
            if len(pron.intersection(pron1)) > 0 and len(pron.intersection(pron2)) > 0:
                print(word)