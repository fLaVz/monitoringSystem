import os.path
import sys

def fonction1():

	for line in sys.stdin:
		#sys.stdout.write(line)
		print line.split()[0]
