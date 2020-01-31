def cumsum(t):
    """Takes a list t of numbers, and returns a new list of the cumulative sums.
    
    t: list of numbers.
    """
    
    res = []
    cumulative_sum = 0
    for s in t:
        cumulative_sum += s
        res.append(cumulative_sum)
    return(res)

print(cumsum([1,2,3,4,5,6]))
print(cumsum([1,0,4,2,5,6]))