	#!/usr/bin/python
 
#Gnuplot.py
# numpy

#from numpy import *

import Gnuplot, Gnuplot.funcutils
import ConfigParser
import os

def plotHistogramm(section):
	config = ConfigParser.ConfigParser()
	point = []
	fichier = []

	#choper les noms des fichiers

	RAM = os.popen('find logs/ -type f -name "*.ini"')
	message = RAM.readlines()
	RAM.close()
	
	if message:

		buffer = 0
		for i in message:
			message[buffer] = message[buffer].strip()
			#message[buffer] = message[buffer].strip('logs/')
			buffer = buffer+1


		#boucle des points
		buffer = 0
		for j in message:
				config.read(message[buffer])
				if(section == "RAM"):				
					x = config.get('RAM','total')
				elif(section == "CPU"):
					x = config.get('CPU','currentfrequency')
				elif(section == "HDD"):
					x = config.get('HDD','total')
				point.append(x)	
				buffer = buffer+1
			
			

		g = Gnuplot.Gnuplot(debug=1)
		g('reset')
		if(section == "RAM"):
			g.title('RAM') # (optional)
			g('set output "graph/RAM.png"')
		elif(section == "CPU"):
			g.title('CPU') # (optional)
			g('set output "graph/CPU.png"')
		elif(section == "HDD"):
			g('set output "graph/HDD.png"')
			g.title('HDD') # (optional)

		#g('set data style linespoints') # give gnuplot an arbitrary command
		g('set terminal png')
		g('set xlabel " Machines "')
		g('set ylabel " Valeurs "')
		g('set style data histograms')
		g('set style fill solid 1.0 border -1')
		#Plot a list of (x, y) pairs (tuples or a numpy array would
		#also be OK):
		g.plot(point)
	else:
		print "Pas de log"
