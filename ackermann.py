def ack(m,n):
    check_int = isinstance(m,int) and isinstance(n,int)
    if not check_int:
        print("Inputs need to be integers.")
    elif not (m >= 0 and n >= 0):
        print("Inputs need to be non-negative integers.")
    elif m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))

print(ack(3,4))