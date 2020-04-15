def rotate_word(word,int):
    """Encrypts (word) using a Caesar cypher, rotating word by the integer (int).
    """
    
    new_word = ''
    for letter in word:
        if 97 <= ord(letter.lower()) <= 122 :
            new_letter = chr((int + ord(letter.lower())-ord('a'))%26 + ord('a'))
        else:
            new_letter = letter
        new_word = new_word + new_letter
    return new_word


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
for word in word_dict:
    for int in range(25):
        if rotate_word(word,int+1) in word_dict:
            print(word, rotate_word(word,int+1),int+1)