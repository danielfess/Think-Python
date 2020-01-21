def is_palindrome(string):
    """Returns True if (string) is a palindrome."""
    return string == string[::-1]

print(is_palindrome('redivider'))
print(is_palindrome('apple'))

def odometer(number):
    """Reduces (number) modulo 1,000,000 and converts to a string of length 6,
    padded by zeroes if necessary."""
    
    number = number%1000000
    string = str(number)
    reading = '0'*(6-len(string)) + string
    return reading

print(odometer(123456))
print(odometer(34))
print(odometer(42313213123456))

print('Possible initial odometer readings below:')

for i in range(1000000):
    string = odometer(i)
    if is_palindrome(string[2:]):
        string = odometer(i+1)
        if is_palindrome(string[1:]):
            string = odometer(i+2)
            if is_palindrome(string[1:5]):
                string = odometer(i+3)
                if is_palindrome(string):
                    print(i)
    