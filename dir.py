import os 
import sys

def find_file(dir, str):
	print dir, str
	for x in os.listdir(dir):
		if os.path.isdir(x):
			x = '.' + os.path.sep + os.path.sep + x
			print x
			find_file(x, str)
		elif os.path.isfile(x) and str in x:
			print os.path.join(os.path.abspath(dir), x)
		else:
			continue

str = sys.argv[1]
find_file('.', str)

