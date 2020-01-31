def is_anagram(string1,string2):
    """Returns True if the two strings are anagrams of each other.
    
    string1, string2: strings
    """
    
    if len(string1) != len(string2):
        return False
    for letter in string1:
        if string1.count(letter) != string2.count(letter):
            return False
    return True

print(is_anagram('word','drow'))
print(is_anagram('words','drow'))
print(is_anagram('word','drows'))
print(is_anagram('words','droow'))
print(is_anagram('words','drowd'))
print(is_anagram('range','anger'))
print(is_anagram('pears','spare'))