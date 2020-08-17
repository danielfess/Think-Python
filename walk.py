import os

def print_filenames(dir):
	"""Prints the names of all files in the directory
	dir and its subdirectories.

	dir: directory

	output: None
	"""

	if os.path.isdir(dir) == False:
		print(dir,'is not a directory.')
	data = os.walk(dir)
	for entry in data:
		for filename in entry[2]:
			print(filename)

print_filenames('C:/users/danie/onedrive/documents/think_python')
print_filenames('C:/users/danie/onedrive/documents/princeton/bristol summer school')