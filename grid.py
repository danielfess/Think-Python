edge = ('+' + (' '+'-')*4 + ' ')*2 + '+'
mid = ('|' + ' '*9)*2 + '|'

def do_twice(f,s):
    f(s)
    f(s)

def do_four(f,s):
    do_twice(f,s)
    do_twice(f,s)

print('2 x 2 grid')
print(edge)
do_four(print,mid)
print(edge)
do_four(print,mid)
print(edge)

print('Testing how to print on same line')
print('+', '-')
print('+',end=' ')
print('-')

print('4 x 4 grid')
dash = (' '+'-')*4 + ' '
spaces = ' '*9
edge4 = ('+' + dash)*4 + '+'
mid4 = ('|' + spaces)*4 + '|'

print(edge4)
do_four(print,mid4)
print(edge4)
do_four(print,mid4)
print(edge4)
do_four(print,mid4)
print(edge4)
do_four(print,mid4)
print(edge4)