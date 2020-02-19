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

word_list = make_word_list()
for word in word_list:
    if word <= word[::-1]:
        if in_bisect(word_list,word[::-1]) != None:
            print(word, word[::-1])