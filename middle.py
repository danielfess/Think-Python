def middle(t):
    """Takes a list t and returns a new list with the first and last
    entries of t deleted.
    
    t: list
    """
    
    return t[1:-1]

t = [1,2,3,4,5,6,'penultimate','final']
s = middle(t)
print(t)
print(s)