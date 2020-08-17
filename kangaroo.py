class Kangaroo:
	"""A class which has attributed to it a pouch,
	which is a list.

	Attributes: name, pouch_contents
	"""

	def __init__(self,name,pouch_contents=None):
		if pouch_contents == None:
			pouch_contents = []
		self.name = name
		self.pouch_contents = pouch_contents

	def put_in_pouch(self,object):
		self.pouch_contents.append(object)

	def __str__(self):
		t = [ self.name + ' has pouch contents:' ]
		for obj in self.pouch_contents:
			s = '    ' + str(obj)
			t.append(s)
		return '\n'.join(t)

if __name__ == '__main__':
	kanga = Kangaroo('kanga',['shopping bag'])
	roo = Kangaroo('roo',['apple','banana'])
	kanga.put_in_pouch(roo)
	kanga.put_in_pouch('chocolate bar')
	print(kanga)
	print(roo)