def histogram(s):
    """Counts the number of times each character appears in the string s.
    
    s: string
    returns: dictionary
    """
    
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

print(histogram('apple'))
print(histogram('redivider'))
print(histogram('exemplified'))

#Some test code to investigate interaction between aliasing and
#global / local variables.

t = [1,2,3]
def example2(t):
    s = t
    s += [4]
    print(s)
    print(t)

example2(t)
print(t)