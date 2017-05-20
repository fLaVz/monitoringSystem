import os
import ConfigParser
import mailer
from termcolor import colored, cprint


#gestion de crise
def check(date, host, cpuIn, hddIn, ramIn, histIn):

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

	# Gestion d'historique
	files = []
	files = os.listdir('logs/')

	# on range en ordre chronologique	
	files.sort()
	# on inverse pour supprimer les plus vieux fichiers
	files.reverse()
	#print files
	for i in range(len(files)):
		if i >= histIn:
			os.remove('logs/'+files[i])
			#print "REMOVED : "+ files[i]

	del files
	print "\n"