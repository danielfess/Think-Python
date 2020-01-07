def do_n(f,n):
    """Calls the function f n times"""
    if n<=0:
        return
    f()
    do_n(f,n-1)

def print_spam():
    print('spam')

do_n(print_spam,7)