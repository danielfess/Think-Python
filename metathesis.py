fin = open('words.txt')
word_dict = dict()
for line in fin:
    word = line.strip()
    word_dict[word] = None

anagram_dict = dict()
fin = open('words.txt')
for line in fin:
    word = line.strip()
    chars = tuple(sorted(word))
    entry = anagram_dict.setdefault(chars,[])
    anagram_dict.setdefault(chars,[]).append(word)



def metathesis(str1,str2):
    """Returns True if the two strings form a metathesis pair.
    
    str1, str2: strings

    output: bool
    """
    
    if sorted(str1) != sorted(str2):
        return False
    differ = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differ += 1
    if differ == 2:
        return True
    return False


metathesis_pairs = []

for key in anagram_dict:
    if len(anagram_dict[key]) > 1:
        for word1 in anagram_dict[key]:
            for word2 in anagram_dict[key]:
                if word1 != word2 and metathesis(word1,word2) and (word2, word1) not in metathesis_pairs:
                    metathesis_pairs.append((word1, word2))

count = 0
for tup in metathesis_pairs:
    count += 1
    if len(tup[0]) > 8:
        print(tup)

print(count)