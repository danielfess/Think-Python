import math
import turtle


def iso_tri(t,angle,side):
    """Draws an isoceles triangle given by a pair of sides of
    equal length (side) and given (angle) between them
    """
    t.fd(side)
    t.lt(90+angle/2)
    t.fd(2*side*math.sin(angle/2*2*math.pi/360))
    t.lt(90+angle/2)
    t.fd(side)
    t.lt(180-angle)

def pie(t,n,radius):
    """Draws a 'turtle pie' of given radius and made of n triangles
    t: turtle
    """
    angle = 360.0/n
    side = radius
    for i in range(n):
        t.lt(angle/2)
        iso_tri(t,angle,side)
        t.lt(angle/2)

def move(t,length):
    """Moves turtle t forward (length) units without leaving a trail.
    Leaves the pen down
    """
    t.pu()
    t.fd(length)
    t.pd()

#Drawing shapes as in Figure 4-2
bob = turtle.Turtle()
move(bob,-125)
pie(bob,5,50)

move(bob,125)
pie(bob,6,50)

move(bob,125)
pie(bob,7,50)

t.hideturtle()

turtle.mainloop()