import copy

class Time:
	"""Represents the time of day, measured in seconds from midnight.

	Attributes: seconds (int)
	"""

	def __init__(self,seconds=0):
		self.seconds = seconds

	def __add__(self,other):
		if isinstance(other,Time):
			return Time(self.seconds + other.seconds)
		elif isinstance(other,int):
			return self.increment2(other)
		else:
			print('Error: Time objects can only be added to each other or to integers')

	def __radd__(self,other):
		return self.__add__(other)

	def int_to_time(self):
		secs, total_mins = self.seconds % 60, self.seconds // 60
		mins, total_hours = total_mins % 60, total_mins // 60
		hours = total_hours % 24
		return hours,mins,secs

	def __str__(self):
		return '%.2d:%.2d:%.2d' % (self.int_to_time())

	def is_after(self,other):
		"""Returns True if the time object self is chronologically after
		the time object other.

		self, other: time objects
		"""

		return self.seconds >= other.seconds

	def increment(self,incr):
		"""Advances the given time object by the given number of seconds.

		incr: non-negative int
		"""

		self.seconds += incr

	def increment2(self,incr):
		"""Returns a new time object with the time advanced by the given
		number of seconds.

		incr: non-negative int
		"""

		return Time(self.seconds + incr)

if __name__ == '__main__':
	t1 = Time(45553)

	t2 = Time(47469)

	t3 = Time(100000)

	t4 = Time(1)

	t5 = Time(86400)

	print(t1)
	print(t2)
	print(t3)
	print(t4)
	print(t5)
	print(t1.is_after(t2))
	print(t2.is_after(t3))
	print(t5.is_after(t5))
	print(t5.is_after(t4))
	t1.increment(46)
	print(t1)
	t1.increment(12)
	print(t1)
	t6 = t1.increment2(115)
	t7 = t1 + 115
	t8 = 115 + t1
	print(t1)
	print(t6)
	print(t7)
	print(t8)