fin = open('words.txt')

def has_no_e(word):
    """Returns True if the string (word) contains no e."""
    
    for letter in word:
        if letter.lower() == 'e':
            return False
    return True

def avoids(word,letters):
    """Returns True if the string (word) avoids all of the letters in (letters).
    All strings need to be in lowercase.
    """
    
    for letter in letters:
        if letter in word:
            return False
    return True

def uses_only(word,letters):
    """Returns True if (word) uses only (letters)."""
    
    for letter in word:
        if letter not in letters:
            return False
    return True

def uses_all(word,letters):
    """Returns True if (word) uses all (letters) at least once."""
    
    return uses_only(letters,word)

def is_abecedarian(word):
    """Returns True if the letters in word are in alphabetical order."""
    
    position = ord('a')
    for letter in word:
        if ord(letter) >= position:
            position = ord(letter)
        else:
            return False
    return True

for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

fin = open('words.txt')

total = 0
count = 0
#letters = input('Input a string of letters to be avoided.\n')
letters = 'aeiou'
for line in fin:
    total = total + 1
    word = line.strip()
    if avoids(word,letters):
        #print(word)
        count = count + 1
print(count)
print(total)
print(count/total*100)

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if uses_only(word,'acefhlo'):
        print(word)

fin = open('words.txt')
letters = input('Input letters which must appear in words.\n')
count = 0
for line in fin:
    word = line.strip()
    if uses_all(word,letters):
        print(word)
        count = count + 1
print(count)

fin = open('words.txt')
count = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
        count = count + 1
print(count)