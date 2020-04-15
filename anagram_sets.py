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

count = 0
for key in anagram_dict:
    if len(anagram_dict[key]) > 1:
        count +=1

def anagrams(word_list):
    """Given a .txt file word_list, prints all anagrams of words appearing
    in word_list.  The file word_list should contain no punctuation except
    spaces.

    word_list: .txt file
    
    output: None
    """
    
    fin = open(word_list)
    anagram_list = []
    for line in fin:
        word = line.strip()
        word = word.lower()
        chars = tuple(sorted(word))
        num = len(anagram_dict[chars])
        anagram_list.append(anagram_dict[chars])
    anagram_list.sort()
    for ana in anagram_list:
        print(ana)

anagrams('anagram_words.txt')

max_anagrams = 0
max_anagrams_list = []
for word in word_dict:
    if len(word) == 8:
        chars = tuple(sorted(word))
        num = len(anagram_dict[chars])
        if num > max_anagrams:
            print(num)
            max_anagrams_list = [chars]
            max_anagrams = num
        elif num == max_anagrams:
            max_anagrams_list.append(chars)

max_anagrams_set = set(max_anagrams_list)
print(max_anagrams_set)
for chars in max_anagrams_set:
    print(anagram_dict[chars])
        
