import mProbe
#import bProbe
#import pProbe

import requestHostname
import datetime
import time
import parser







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
	F = open(hostname+'_'+dateHour+'.ini','w')

	#Parse
	parser.parse()

	#Probe Part
	mProbe.getRAM(dateHour,hostname)

	#bProbe.getUsers(
	#bProbe.getProcess(

	#pProbe.getCPU(
	#pProbe.getHDD(

	#Time
	time.sleep(5.0 - ((time.time() - starttime) % 5.0))
