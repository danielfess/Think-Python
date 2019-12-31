def right_justify(s):
    length = len(s)
    spaces = ' '*(70-length)
    newstr = spaces + s
    print(newstr)

right_justify('free willy')