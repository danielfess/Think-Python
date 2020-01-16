def gcd(a,b):
    """Returns the GCD of two non-negative integers a,b."""
    
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print(gcd(0,4))
print(gcd(4,0))
print(gcd(2,6))
print(gcd(6,2))
print(gcd(45,105))
print(gcd(30,69))