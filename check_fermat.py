def check_fermat(a,b,c,n):
    """Check's if fermat's equation a**n + b**n = c**n is satisfied.
    a, b, c: integers
    n: positive integer
    """
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    if n<=2:
        print('n>2 required')
    elif a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")

check_fermat(3.000,4,5,2)
check_fermat(3,4,6,2)
check_fermat(1.0,4,543,14)