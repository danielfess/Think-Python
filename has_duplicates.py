def has_duplicates(list):
    """Takes a list and returns True if the list contains duplicates.
    
    list: list
    """
    
    for item in list:
        if list.count(item) > 1:
            return True
    return False

print(has_duplicates(['a','b','a','c']))
print(has_duplicates(['a','b1','b',1,3,4]))
print(has_duplicates(['apple','plea','pleap']))

list = ['a','b','c']
print(has_duplicates(list))
print(list)