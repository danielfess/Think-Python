def recurse(n, s):
    """Given a non-negative integer n and a number s, computes the n-th
    triangle number plus s.
    """
    if n== 0:
        print(s)
    else:
        recurse(n-1,n+s)

recurse(3,0)
recurse(3,1)
recurse(3,4)
recurse(4,0)