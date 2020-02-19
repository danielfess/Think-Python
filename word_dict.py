def word_dict():
    """Takes the words in words.txt and creates a dictionary from them.
    
    returns: dictionary
    """

    d = dict()
    file = open('words.txt')
    for line in file:
        word = line.strip()
        d[word] = 0
    return d


def is_word_in_dict(word,d):
    """Returns True if word is a key in the dictionary d.

    word: string
    d: dictionary

    returns: bool
    """
    
    return word in d

d = word_dict()

print(is_word_in_dict('apple',d))
print(is_word_in_dict('appley',d))
print(is_word_in_dict('combination',d))
print(is_word_in_dict('combinator',d))

file = open('words.txt')
wordlist = []
for line in file:
    word = line.strip()
    wordlist.append(word)

print('Testing speed of is_word_dict')
for i in range(100):
    print(is_word_in_dict(wordlist[i],d))

print('See inlist.py for comparison with two analogous list methods')