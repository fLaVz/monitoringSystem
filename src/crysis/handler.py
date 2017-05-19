import os
import ConfigParser
import mailer
from termcolor import colored, cprint


config = ConfigParser.ConfigParser()

config.read('test2.ini')
config.sections()

cpuMax = config.get('CPU', 'maxfrequency')
HDDspace = config.get('HDD', 'space')

if int(cpuMax) > 3500:
	cprint ("cpu load too high: " + cpuMax + "Mhz", 'white', 'on_red')
	#mailer.sendMailAlert("cpu load too high")
else:
	cprint ("cpu ok: " + cpuMax + "Mhz", 'white', 'on_green')

if int(HDDspace) > 90:
	cprint ("HDD almost full : " + HDDspace + "% used", 'white', 'on_red')
	#mailer.sendMailAlert("HDD almost full")
else: 
	cprint ("Disk ok: " + HDDspace + "% used", 'white', 'on_green')

files = []
files = os.listdir('.')

print files[len(os.listdir('.'))-1]


