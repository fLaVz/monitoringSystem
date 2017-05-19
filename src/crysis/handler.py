import os
import ConfigParser
import mailer


config = ConfigParser.ConfigParser()

config.read('test2.ini')
config.sections()

cpuMax = config.get('CPU', 'maxfrequency')
HDDspace = config.get('HDD', 'space')

print cpuMax

if int(cpuMax) > 3500:
	print "cpu load too high"
	#mailer.sendMailAlert("cpu load too high")
else:
	print "cpu ok"

if int(HDDspace) > 90:
	print "HDD almost full" 
	#mailer.sendMailAlert("HDD almost full")
else:
	print "Disk ok"

files = []
files = os.listdir('.')

print files[len(os.listdir('.'))-1]


