import time

def timeofday():
    """Prints current time of day in 24 hour format,
    along with days since 1st Jan 1970.
    """
    t = time.time() #time in seconds since 1st Jan 1970
    seconds = str(int(t%60))
    minutes = str(int((t//60)%60))
    hours = str(int((t//3600)%24))
    days = str(int(t//(3600*24)))
    seconds = zeropad(seconds)
    minutes = zeropad(minutes)
    hours = zeropad(hours)
    s = '(days since epoch ='+days+', current time = '+hours+':'+minutes+':'+seconds+')'
    print(s)

def zeropad(s):
    """Pads a one digit integer presented as a string with a zero in the front.
    Leaves other integer as they are."""
    if len(s) == 1:
        s = '0'+s
    return s

#Testing zeropad
print('8')
print(len('8'))
print(zeropad('24'))
print(zeropad('8'))

timeofday()
