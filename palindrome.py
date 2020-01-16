def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

print(first('abc'))
print(middle('abc'))
print(last('abc'))

print(first('ab'))
print(middle('ab'))
print(last('ab'))

print(first('a'))
print(middle('a'))
print(last('a'))

#print(first(''))
print(middle(''))
#print(last(''))

def is_palindrome(word):
    """Returns True if the string (word) is a palindrome."""
    
    if len(word) == 0:
        return True
    elif first(word) == last(word):
        return is_palindrome(middle(word))
    else:
        return False

print(is_palindrome('aba'))
print(is_palindrome('redivider'))
print(is_palindrome('redivsider'))
print(is_palindrome('redet'))
print(is_palindrome(' '))
print(is_palindrome(''))