def print_spam():
    print('spam')

def do_twice(f,s):
    f(s)
    f(s)

def print_twice(bruce):
    print(bruce)
    print(bruce)

print('do_twice + print_twice:')
do_twice(print_twice,'spam')

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)

print('do_four:')
do_four(print,'spam')

print('do_twice type:')
print(type(do_twice(print,'spam')))