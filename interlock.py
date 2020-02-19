def make_word_list():
    """Creates a sorted list from the words in words.txt
    
    returns: list of words (as strings)
    """

    file = open('words.txt')
    list = []
    for line in file:
        word = line.strip()
        list.append(word)
    return list

def in_bisect(t,target):
    """If target is in the sorted list t, returns the index of target.  If
    target is not in the sorted list t, returns None.
    
    t: sorted list
    target: value
    
    returns: integer index, or None
    """
    
    s = t[:]
    index = 0
    while len(s) > 1:
        halfway = int(len(s)/2)
        if target <= s[halfway-1]:
            s = s[:halfway]
        else:
            s = s[halfway:]
            index += halfway
    if target in s:
        return index

def two_way_interlock():
    """Prints all pairs of interlocking words and their result.
    
    returns: None
    """
    
    word_list = make_word_list()
    for word in word_list:
        if (in_bisect(word_list,word[::2]) != None and
            in_bisect(word_list,word[1::2]) != None):
            print(word[::2], word[1::2],word)

def n_way_interlock(n):
    """Prints all n-tuples of interlocking words and their result.
    
    returns: None
    """
    
    word_list = make_word_list()
    for word in word_list:
        if all(in_bisect(word_list,word[i::n]) != None for i in range(n)):
            string = ''
            for i in range(n):
                string += word[i::n] + ' '
            string += word
            print(string)

n_way_interlock(3)

