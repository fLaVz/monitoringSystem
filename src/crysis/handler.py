import os
import ConfigParser

config = ConfigParser.ConfigParser()

config.read('test.ini')
config.sections()

cpuMax = config.get('CPU', 'maxfrequency')

if cpuMax > 3500
	print "cpu load too high"
elif HDDspace > 90%
	print "HDD almost full" 

files = []
files = os.listdir('.')

print files[len(os.listdir('.'))-1]