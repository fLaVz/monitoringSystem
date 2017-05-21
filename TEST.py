#!/usr/bin/python
 
#Gnuplot.py
# numpy

#from numpy import *

import Gnuplot, Gnuplot.funcutils
import ConfigParser
import os

def plotHistogramm(host,section):
	config = ConfigParser.ConfigParser()
	point = []
	fichier = []

#choper les noms des fichiers

	RAM = os.popen('find logs/ -type f -name "*.ini"')
	message = RAM.readlines()
	RAM.close()

	for i in message:
		fichier.append(message[i])


#boucle des points
	for j in fichier:
		config.read(fichier[j])
		if(section == "RAM")
			x = config.get('RAM','total')
		else if(section == "CPU")
			x = config.get('CPU','currentfrequency')
		else if(section == "HDD")
			x = config.get('HDD','total')
		point.append(x)



	g = Gnuplot.Gnuplot(debug=1)
	g('reset')
	g.title('A simple example') # (optional)
	#g('set data style linespoints') # give gnuplot an arbitrary command
	g('set output "myGraph.png"')
	g('set terminal png')
	g('set xlabel " bite "')
	g('set ylabel " chatte "')
	g('set style data histograms')
	g('set style fill solid 1.0 border -1')
	# Plot a list of (x, y) pairs (tuples or a numpy array would
	# also be OK):
	g.plot(point)
