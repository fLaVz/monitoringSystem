import os
import ConfigParser
import mailer
from termcolor import colored, cprint


#gestion de crise
def check(date, host, cpuIn, hddIn, ramIn):

	cprint ("************** CRITICAL MODULE ********************", 'cyan', 'on_white')

	config = ConfigParser.ConfigParser()
	config.read('logs/'+host+'_'+date+'.ini')
	config.sections()

	cpuMax = config.get('CPU', 'currentfrequency')
	HDDspace = config.get('HDD', 'percent')
	ramTot = config.get('RAM', 'total')
	ramAv = config.get('RAM', 'disponible')
	ramPercent = 100 - ((100*float(ramAv))/float(ramTot))

	if float(cpuMax) > cpuIn:
		cprint ("cpu load too high: " + cpuMax + "Mhz", 'white', 'on_red')
		#mailer.sendMailAlert(host, "cpu load too high")
	else:
		cprint ("cpu ok: " + cpuMax + "Mhz", 'white', 'on_green')

	if float(HDDspace) > hddIn:
		cprint ("HDD almost full : " + HDDspace + "% used", 'white', 'on_red')
		#mailer.sendMailAlert(host, "HDD almost full")
	else: 
		cprint ("Disk ok: " + HDDspace + "% used", 'white', 'on_green')

	if float(ramPercent) > ramIn:
		cprint ("RAM almost fully used: " + str(ramPercent) + "% used", 'white', 'on_red')
		#mailer.sendMailAlert(host, "High Ram usage")
	else: 
		cprint ("Ram usage ok: " + str(ramPercent) + "% used", 'white', 'on_green')




	files = []
	files = os.listdir('.')

	print files[len(os.listdir('.'))-1]
	print "\n"