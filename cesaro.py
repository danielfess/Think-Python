import turtle

def cesaro(t,x,angle):
    """Draw a Cesaro fractal curve of length x, with the iteratively added
    triangles defined by (angle).
    angle: 0 <= angle < 90.
    t: turtle.
    """
    
    if x<10:
        t.fd(x)
    else:
        cesaro(t,x/4,angle)
        t.lt(angle)
        cesaro(t,x/4,angle)
        t.rt(2*angle)
        cesaro(t,x/4,angle)
        t.lt(angle)
        cesaro(t,x/4,angle)

bob = turtle.Turtle()

def cesaro_snowflake(t,x,angle):
    """Draw a cesaro snowflake of length x given by (angle).  t: turtle."""
    for i in range(3):
        cesaro(t,x/3,angle)
        t.rt(120)

cesaro_snowflake(bob,500,40)
turtle.mainloop()