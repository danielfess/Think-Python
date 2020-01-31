def is_sorted(t):
    """Returns True if the list t is in ascending order.
    
    t: list of items which may be ordered e.g. numbers, strings.
    """
    
    i = 0
    while i < len(t)-1:
        if t[i] > t[i+1]:
            return False
        i += 1
    return True

print(is_sorted([1,2,2]))
print(is_sorted([1,3,2]))
print(is_sorted(['a','b']))
print(is_sorted(['a','aa','ab','b']))
print(is_sorted(['aa','a','ab','b']))
print(is_sorted(['2','a','aa','ab','b']))
print(is_sorted(['a','aa','ab','b','2']))
print(is_sorted(['1','12a','2','2a','a','a2','aa','ab','b']))