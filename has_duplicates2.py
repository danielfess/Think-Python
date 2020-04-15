def has_duplicates2(t):
    """Returns True if the list t contains duplicates.
    
    t: list
    
    returns: bool
    """
    
    d = dict()
    for s in t:
        if s in d:
            return True
        else:
            d[s] = None
    print(d)
    return False

print(has_duplicates2([1,2,3,4,5]))
print(has_duplicates2([1,2,2,3,4]))