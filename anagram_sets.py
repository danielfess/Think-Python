def make_word_dict():

    fin = open('words.txt')
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict[word] = None

def make_anagram_dict():
    
    word_dict = make_word_dict() 
    anagram_dict = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        chars = ''.join(sorted(word))
        anagram_dict.setdefault(chars,[]).append(word)
    return anagram_dict

def anagrams(word_list):
    """Given a .txt file word_list, prints all anagrams of words appearing
    in word_list.  The file word_list should contain no punctuation except
    spaces.

    word_list: .txt file
    
    output: None
    """
    
    anagram_dict = make_anagram_dict()
    fin = open(word_list)
    anagram_list = []
    for line in fin:
        word = line.strip()
        word = word.lower()
        chars = ''.join(sorted(word))
        num = len(anagram_dict[chars])
        anagram_list.append(anagram_dict[chars])
    anagram_list.sort()
    for ana in anagram_list:
        print(ana)

def max_anagrams():
    word_dict = make_word_dict()
    anagram_dict = make_anagram_dict()
    max = 0
    max_anagrams_list = []
    for word in word_dict:
        if len(word) == 8:
            chars = ''.join(sorted(word))
            num = len(anagram_dict[chars])
            if num > max:
                print(num)
                max_anagrams_list = [chars]
                max = num
            elif num == max:
                max_anagrams_list.append(chars)
    
    max_anagrams_set = set(max_anagrams_list)
    print(max_anagrams_set)
    for chars in max_anagrams_set:
        print(anagram_dict[chars])

if __name__ == '__main__':
    anagrams('anagram_words.txt')
    
    anagram_dict = make_anagram_dict()
    count = 0
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count +=1
    print(count)