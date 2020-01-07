import turtle

def koch(t,x):
    """Draw a Koch curve of length x. t: turtle."""
    if x<10:
        t.fd(x)
    else:
        koch(t,x/4)
        t.lt(60)
        koch(t,x/4)
        t.rt(120)
        koch(t,x/4)
        t.lt(60)
        koch(t,x/4)

bob = turtle.Turtle()

def snowflake(t,x):
    """Draw a snowflake of length x.  t: turtle."""
    for i in range(3):
        koch(t,x/3)
        t.rt(120)

snowflake(bob,4000)
turtle.mainloop()