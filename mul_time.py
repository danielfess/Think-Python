class Time:
	"""Represents the time of day.

	Attributes: hour, minute, second
	"""

	def time_to_num(self):
		return self.second + 60*self.minute + 3600*self.hour

def print_time(time):
	"""Prints Time object, with seconds rounded down to
	the nearest integer.

	time: Time object
	output: None
	"""

	string = '%.2d:%.2d:%.2d' % (time.hour,time.minute,time.second)
	print(string)

def time_to_num(time):
	"""Converts a Time object to a number, via a base 60
	to base 10 transformation.

	time: Time object
	output: non-negative int or float
	"""

	return time.second + 60*time.minute + 3600*time.hour

def divmod(n,d):
	"""Returns the quotient and remainder when n is divided
	by d.

	n: int or float
	d: int
	output: int, int or float
	"""

	return n//d, n%d

def num_to_time(num):
	"""Inverse of time_to_int

	num: non-negative int or float
	output: Time object
	"""

	time = Time()
	minutes, time.second = divmod(num,60)
	time.hour, time.minute = divmod(minutes,60)
	return time

def mul_time(time,n):
	"""Returns a new Time object whose time is given by
	multiplying the given Time object by the number n.

	time: Time object
	n: non-negative int or float
	output: Time object
	"""

	seconds = time.time_to_num()
	t2 = num_to_time(n*seconds)
	return t2

def avg_pace(time,distance):
	"""Returns the average pace (time per mile) for a race
	of given distance in miles with given finishing time.

	time: Time object
	distance: non-negative int or float
	"""

	return mul_time(time,1/distance)

if __name__ == '__main__':
	t1 = Time()
	t1.hour = 0
	t1.minute = 28
	t1.second = 35
	distance = 4
	pace = avg_pace(t1,distance)
	print_time(pace)

