import math
import copy

class Circle:
	"""Represents a circle.

	Attributes: center, radius
	"""

class Point:
	"""Describes a point in two-dimensional space

	Attributes: x, y coordinates
	"""

class Rectangle:
	"""Describes a horizontal/vertical rectangle in
	2-d space.

	Attributes: width, height, corner
	Note: corner is bottom left corner.
	"""

def distance(p1,p2):
	"""Computes the distance between two points in
	2-d space.

	p1, p2: instance of Point
	"""

	x1, y1, x2, y2 = p1.x, p1.y, p2.x, p2.y
	return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def point_in_circle(circle,point):
	"""Returns True if point lies on or inside circle.

	circle: instance of Circle
	point: instance of Point
	"""

	return distance(point,circle.center) <= circle.radius

def move_point(point,dx,dy):
	"""Moves a point right by dx and up by dy, then
	returns the new point.  Does not change original point.

	point: instance of Point
	dx, dy: floating point numbers
	"""

	new_point = copy.copy(point)
	new_point.x += dx
	new_point.y += dy
	return new_point

def rect_corners(rect):
	"""Returns a list of the four corners of a rectangle.

	rect: instance of Rectangle
	"""

	p = []
	p.append(rect.corner)
	p.append(move_point(rect.corner,rect.width,0))
	p.append(move_point(rect.corner,0,rect.height))
	p.append(move_point(rect.corner,rect.width,rect.height))
	return p

def rect_in_circle(circle,rect):
	"""Returns True if the rectangle 'rect' lies entirely
	on or inside the circle.

	circle: instance of Circle
	rect: instance of Rectangle
	"""

	p = rect_corners(rect)
	for i in range(4):
		if not point_in_circle(circle,p[i]):
			return False
	return True

def rect_circle_overlap(circle,rect):
	"""Returns True if any of the corners of the rectangle
	'rect' lie on or inside the circle.

	circle: instance of Circle
	rect: instance of Rectangle
	"""

	p = rect_corners(rect)
	for i in range(4):
		if point_in_circle(circle,p[i]):
			return True
	return False

def rect_circle_overlap2(circle,rect):
	"""Returns True if any part of the rectangle 'rect'
	lies on or inside the circle.

	circle: instance of Circle
	rect: instance of Rectangle
	"""

	x = circle.center.x - rect.corner.x
	y = circle.center.y - rect.corner.y
	
	if x < 0:
		dx = 0
	elif x > rect.width:
		dx = rect.width
	else:
		dx = x
	
	if y < 0:
		dy = 0
	elif y > rect.height:
		dy = rect.height
	else:
		dy = y
	
	shifted_circle_center = Point()
	shifted_circle_center.x = x
	shifted_circle_center.y = y
	nearest_point = Point()
	nearest_point.x = dx
	nearest_point.y = dy
	if distance(nearest_point,shifted_circle_center) <= circle.radius:
		return True
	else:
		return False


if __name__ == '__main__':
	c = Circle()
	c.center = Point()
	c.center.x = 150
	c.center.y = 100
	c.radius = 75

	r1 = Rectangle()
	r1.corner = Point()
	r1.corner.x = 150
	r1.corner.y = 100
	r1.width = 40
	r1.height = 50

	r2 = Rectangle()
	r2.corner = Point()
	r2.corner.x = 130
	r2.corner.y = 90
	r2.width = 80
	r2.height = 70

	r3 = Rectangle()
	r3.corner = Point()
	r3.corner.x = 200
	r3.corner.y = 0
	r3.width = 50
	r3.height = 200

	print(rect_in_circle(c,r1))
	print(rect_in_circle(c,r2))
	print(rect_in_circle(c,r3))
	print(rect_circle_overlap(c,r1))
	print(rect_circle_overlap(c,r2))
	print(rect_circle_overlap(c,r3))
	print(rect_circle_overlap2(c,r1))
	print(rect_circle_overlap2(c,r2))
	print(rect_circle_overlap2(c,r3))



