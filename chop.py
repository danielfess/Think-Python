def chop(t):
    """Modifies a list t by removing the first and last entries.
    Returns None.
    
    t: list
    """
    
    del t[0]
    del t[-1]

t = [1,2,3,4,5,6,'penultimate','final']
s = chop(t)
print(t)
print(type(s))
print(t)