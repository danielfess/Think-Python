file = open('words.txt')
list = []
for line in file:
    word = line.strip()
    list.append(word)

def in_bisect(t,target):
    """If target is in the sorted list t, returns the index of target.  If
    target is not in the sorted list t, returns None.
    
    t: sorted list
    target: value
    
    returns: integer index, or None
    """
    
    s = t[:]
    index = 0
    while len(s) > 1:
        halfway = int(len(s)/2)
        if target <= s[halfway-1]:
            s = s[:halfway]
        else:
            s = s[halfway:]
            index += halfway
    if target in s:
        return index

print(in_bisect([1,2,3,4,5],5))
print(in_bisect([1,2,2,5,5],2))
print(in_bisect(list,'apple'))
print('apple' in list)
print(in_bisect(list,'snoring'))
print('snoring' in list)
print(list[4450])
print(list[93004])

print('Testing speed of list in operator')
for i in range(100):
    print(list[i] in list)

print('Testing speed of in_bisect')
for i in range(100):
    print(in_bisect(list,list[i]))