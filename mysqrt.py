def mysqrt(a):
    """Estimates the square root of non-negative number (a)."""
    
    x = a
    epsilon = 10**(-15)
    while True:
        y = (x+a/x)/2
        if abs(x-y) < epsilon:
            break
        x = y
    return y

def test_square_root():
    """Prints a table of square roots and estimates."""
    
    print('a' + ' '*3 + 'mysqrt(a)' + ' '*5 + 'math.sqrt(a)' + ' '*2 + 'diff')
    print('-'*len('a') + ' '*3 + '-'*len('mysqrt(a)') + ' '*5 + '-'*len('math.sqrt(a)') + ' '*2 + '-'*len('diff'))
    for i in range(9):
        i=i+1
        index = str(float(i)) + ' '
        estimate = mysqrt(i)
        root = math.sqrt(i)
        estimate_truncated = truncate(str(estimate),13)
        root_truncated = truncate(str(root),13)
        estimate_str = estimate_truncated + ' '*(14-len(estimate_truncated))
        root_str = root_truncated + ' '*(14-len(root_truncated))
        diff = abs(estimate - root)
        if str(diff)[len(str(diff))-4] == 'e':
            diff_str = truncate(str(diff),13) + str(diff)[len(str(diff))-4:len(str(diff))]
        else:
            diff_str = truncate(str(diff),13)
        print(index + estimate_str + root_str + diff_str)

def truncate(string,length):
    """Truncates (string) to be at most (length) long."""
    
    return string[0:length]

import math
test_square_root()