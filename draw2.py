import circle
import turtle
import math

def draw_rect(t,rect):
	"""Draws the rectangle 'rect' using the turtle t.

	t: turtle
	rect: instance of Rectangle
	"""

	t.pu()
	t.goto(rect.corner.x,rect.corner.y)
	t.pd()
	for i in range(2):
		t.fd(rect.width)
		t.lt(90)
		t.fd(rect.height)
		t.lt(90)

def draw_circle(t,circle):
	"""Draw the circle using the turtle t.

	t: turtle
	circle: instance of Circle
	"""

	r = circle.radius
	steps = 50
	angle_step = 360/steps
	t.pu()
	t.goto(circle.center.x,circle.center.y)
	t.fd(r)
	t.lt(90)
	t.pd()
	for i in range(steps):
		t.fd(2*math.pi*r/steps)
		t.lt(angle_step)


if __name__ == '__main__':
	t = turtle.Turtle()

	r1 = circle.Rectangle()
	r1.corner = circle.Point()
	r1.corner.x = 150
	r1.corner.y = 100
	r1.width = 40
	r1.height = 50

	r2 = circle.Rectangle()
	r2.corner = circle.Point()
	r2.corner.x = 130
	r2.corner.y = 90
	r2.width = 80
	r2.height = 70

	r3 = circle.Rectangle()
	r3.corner = circle.Point()
	r3.corner.x = 200
	r3.corner.y = 0
	r3.width = 50
	r3.height = 200

	c = circle.Circle()
	c.center = circle.Point()
	c.center.x = 150
	c.center.y = 100
	c.radius = 75

	draw_rect(t,r1)
	draw_rect(t,r2)
	draw_rect(t,r3)
	draw_circle(t,c)
	
	turtle.mainloop()
