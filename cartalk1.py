def double_letter(word,i):
    """Returns True if the i-th and i+1-th letters of (word) are equal."""
    
    return word[i] == word[i+1]

print(double_letter('apple',0))
print(double_letter('apple',1))
print(double_letter('apple',2))

def consecutive_doubles(word):
    """Returns True if word contains 3 consecutive double letters."""
    
    for i in range(len(word)-5):
        if double_letter(word,i):
            if double_letter(word,i+2):
                if double_letter(word,i+4):
                    return True
    return False

print(consecutive_doubles('appllyy'))
print(consecutive_doubles('abbccdaa'))

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if consecutive_doubles(word):
        print(word)