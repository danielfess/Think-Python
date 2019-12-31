import turtle
import math

def circle(t,r,n):
    for i in range(n):
        t.fd(2*math.pi*r/n)
        t.lt(360/n)
    turtle.mainloop()

bob = turtle.Turtle()
circle(bob,12,100)