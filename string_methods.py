str = 'old_old_old_fruit'

print(str.replace('old','new'))
print(str.replace('old','new',2))
print(str.partition('d_ol'))
print(str.center(20))
print(str.center(20,'s'))
print(str.lstrip('laborious'))
print(str.lstrip('l'))
print(str.rjust(20,'s'))

str2 = 'lalalalal'

print(str2.count('lal',0,6))
print(str2.count('lal',1,6))
print(str2.startswith(('al','lalal'),0,4))
print(str2.startswith(('al','lalal'),0,5))

str3 = 'banana'
print(str3.count('a'))

def is_palindrome(s):
    """Returns True if the string s is a palindrome.
    Returns False otherwise.
    """
    return s == s[::-1]

print(is_palindrome('sas'))
print(is_palindrome('says'))

def any_lowercase1(s):
    """Returns True if the first character in the string s is lowercase."""
    
    for c in s:
        print(c)
        print('c')
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1('hi'))
print(any_lowercase1('Hi'))

def any_lowercase5(s):
    """Returns True if all characters in the string s are lowercase."""
    
    for c in s:
        if not c.islower():
            return False
    return True

print(any_lowercase5('Hi'))
print(any_lowercase5('hi'))
print(any_lowercase5('hI'))
print(any_lowercase5('hi5'))
