#-*- coding: utf-8 -*-
import mProbe
import pProbe
import handler
import sender
import graph

import requestHostname
import datetime
import time
import parser
import subprocess
import ConfigParser
import os

from os.path import exists


print "********************** Bienvenue dans la gestion des sondes ******************************\n"
cpuIn = input("Veuillez entrer une valeur de situation de crise pour le CPU (en MHz) :")
hddIn = input("Veuillez entrer une valeur de situation de crise pour le Disque (en %) :")
ramIn = input("Veuillez entrer une valeur de situation de crise pour la RAM (en %) :")
histIn = input("Veuillez entrez le nombre maximal de fichiers de configuration a garder sur le disque : ")


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

	print "******************** FROM " + hostname + " **************************"

	

	#Probe Part
	mProbe.getRAM(dateHour,hostname)

	pProbe.getCPU(dateHour,hostname)
	pProbe.getHDD(dateHour,hostname)

	subprocess.call(['./bProbe.sh'])

	#Parse
	parser.parse(dateHour, hostname)

	handler.check(dateHour,hostname, cpuIn, hddIn, ramIn, histIn)

	sender.sendRequest(dateHour, hostname)

	F.close()

	graph.plotHistogramm("RAM")
	graph.plotHistogramm("CPU")
	graph.plotHistogramm("HDD")
	#Time
	time.sleep(5.0 - ((time.time() - starttime) % 5.0))
