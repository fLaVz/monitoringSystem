import mProbe
#import bProbe
import pProbe
import handler

import requestHostname
import datetime
import time
import parser
import subprocess


print "********************** Bienvenue dans la gestion des sondes ******************************\n"
cpuIn = input("Veuillez entrer une valeur de situation de crise pour le CPU (en MHz) :")
hddIn = input("Veuillez entrer une valeur de situation de crise pour le Disque (en %) :")
ramIn = input("Veuillez entrer une valeur de situation de crise pour la RAM (en %) :")


starttime=time.time()
while True:

	#Date
	date = datetime.datetime.now()
	dateHour = str(date)
	dateHour = dateHour.replace(" ","_")
	dateHour = dateHour[:-7]

	#HostName
	hostname = requestHostname.getHostname()

	#ini File
	F = open('logs/'+hostname+'_'+dateHour+'.ini','w')

	#Parse
	parser.parse()

	#Probe Part
	mProbe.getRAM(dateHour,hostname)

#	subprocess.call(['./bProbe.sh'])

	pProbe.getCPU(dateHour,hostname)
	pProbe.getHDD(dateHour,hostname)

	handler.check(dateHour,hostname, cpuIn, hddIn, ramIn)

	F.close()

	#Time
	time.sleep(5.0 - ((time.time() - starttime) % 5.0))
