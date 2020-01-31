print(sum([7,2,3]))

def nested_sum(t):
    """Given a list, t, of lists of numbers, sums the numbers from all the
    nested lists making up t.
    
    t: list of lists of numbers
    """

    res = []
    for s in t:
        total = sum(s)
        res += [total]
    print(res)
    return sum(res)


print(nested_sum([[1],[2]]))
print(nested_sum([[1,2,],[3],[4,5,6],[]]))