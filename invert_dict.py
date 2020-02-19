def invert_dict(d):
    """Inverts the dictionary d.
    
    d: dictionary

    returns: dictionary
    """

    inverse = {}
    print(type(inverse))
    for key in d:
        val = d[key]
        test = inverse.setdefault(val,[key])
        if test != [key]:
            inverse[val].append(key)
    return inverse

print(invert_dict({'p':1, 'a':1, 'r':2, 'o':1, 't':1}))
print(invert_dict({'p':2, 'p':1, 'a':1, 'r':2, 'o':1, 't':1}))
print(invert_dict({'p':1, 'p':2, 'a':1, 'r':2, 'o':1, 't':1}))
#Strange....dictionaries with identical keys behave badly.