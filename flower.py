import math
import turtle


def square(t, length):
    """Draws a square with sides of the given length.

    Returns the Turtle to the starting position and location.
    """
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    """Draws a polygon with n sides.

    t: Turtle
    n: number of sides
    length: length of each side.
    """
    angle = 360.0/n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle.

    t: Turtle
    r: radius
    angle: angle subtended by the arc, in degrees
    """
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 3
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    t.lt(step_angle/2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle/2)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle
    r: radius
    """
    arc(t, r, 360)

def flower(t,n,length):
    """Draw a flower with n petals, with centre t (=Turtle),
    and each petal of arclength = length.
    """
    angle = 540/n
    radius = 360*length/(2*angle*math.pi)
    arc(t,radius,angle)
    t.lt(180-angle)
    for i in range(n-1):
        arc(t,radius,2*angle)
        t.lt(180-angle)
    arc(t,radius,angle)
    turtle.mainloop()

bob = turtle.Turtle()
flower(bob,7,200)

#There are two key pieces of information in this problem: the angle subtended by a petal, and the number of distinct petals.
#Coding the problem in a clean way while taking into account both these variables is a little awkward.
#See Exercise 4-2 in book and according solution online for one way to deal with this.