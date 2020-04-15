known = dict()


def ackermann_memo(m,n):
    """Calculates the ackermann function recursively while storing the
    results of the recursive calls.
    
    m,n: non-negative integers
    
    returns: integer
    """

    if (m,n) in known:
        return known[(m,n)]
    elif m == 0:
        return known.setdefault((m,n), n+1)
    elif n == 0:
        a = ackermann_memo(m-1,1)
        return known.setdefault((m,n),a)
    else:
        a = ackermann_memo(m,n-1)
        b = ackermann_memo(m-1,a)
        return known.setdefault((m,n),b)

print(known)
print(ackermann_memo(0,0))
print(known)
print(ackermann_memo(0,2))
print(known)
print(ackermann_memo(3,2))
print(known)
print(ackermann_memo(3,4))
