word_dict = dict()
fin = open('words.txt')
for line in fin:
    word = line.strip()
    word_dict[word] = None
word_dict['i'] = None
word_dict['a'] = None
word_dict[''] = None

def children(word):
    """Returns a list of the children of a word.  A child is a new word
    formed by removing one character from the string word.

    word: string of length >= 1

    output: list
    """

    l = []
    for i in range(len(word)):
        new_word = word[:i] + word[i+1:]
        if new_word in word_dict and (i == 0 or (i > 0 and word[i] != word[i-1])):
            l.append(new_word)
    return l

reducible_dict = dict()

def reducible(word, bool = False):
    """Returns True if word is reducible.
    Optional bool allows for verbose output.

    word: string

    output: bool
    """

    if word in reducible_dict:
        return reducible_dict[word]
    if word == '':
        reducible_dict[word] = True
        return True
    for child in children(word):
        if reducible(child, bool):
            if bool == True:
                print(word, child)
            reducible_dict[word] = True
            return True
    reducible_dict[word] = False
    return False

for word in word_dict:
    reducible(word, True)

max_length = 0
max_list = []
for word in reducible_dict:
    if reducible_dict[word]:
        if len(word) > max_length:
            max_length = len(word)
            max_list = [word]
        elif len(word) == max_length:
            max_list.append(word)
print(max_length)
print(max_list)