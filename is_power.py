def is_power(a,b):
    """Returns True if a is a power of b.  a,b: positive integers."""
    
    if a == 1:
        return True
    elif b == 1:
        return False
    elif a%b == 0:
        return is_power(a/b,b)
    else:
        return False

print(is_power(9,3))
print(is_power(3,9))
print(is_power(27,9))
print(is_power(81,9))
print(is_power(45,3))
print(is_power(1,4))
print(is_power(4,1))
print(is_power(1,1))