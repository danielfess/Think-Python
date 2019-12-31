import turtle
import math

def arc(t,r,angle,n):
    for i in range(n):
        t.fd(2*math.pi*r*angle/n/360)
        t.lt(angle/n)
    turtle.mainloop()

bob = turtle.Turtle()
arc(bob,50,120,50)