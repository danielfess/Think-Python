class Point():
	"""Represents a point in two-dimensional space

	Attributes: x, y
	"""

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __str__(self):
		return '%g,%g' % (self.x,self.y)

	def __add__(self,other):
		if isinstance(other,Point):
			return self.add_point(other)
		else:
			return self.add_tuple(other)

	def add_point(self,other):
		return Point(self.x + other.x, self.y + other.y)

	def add_tuple(self,other):
		return Point(self.x + other[0], self.y + other[1])

	def __radd__(self,other):
		return self.__add__(other)

if __name__ == '__main__':
	pt = Point()
	print(pt)
	pt.x = 10
	pt.y = 20
	print(pt)
	pt2 = Point(-10,40)
	print(pt2)
	print(pt + pt2)
	pt3 = (20,30)
	print(pt3)
	print(pt + pt3)
	print(pt3 + pt)
