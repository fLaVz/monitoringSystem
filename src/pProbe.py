import psutil
import ConfigParser
import socket
from termcolor import colored, cprint

def getCPU(date, host):

	config = ConfigParser.ConfigParser()
	config.read('logs/'+host+'_'+date+'.ini')


	# CPU PART
	freq = psutil.cpu_freq()
	currentFreq = freq[0]
	minFreq = freq[1]
	maxFreq = freq[2]

	config.add_section('CPU')
	config.set('CPU', 'CurrentFrequency', str(currentFreq))	#CurrentFrequency
	config.set('CPU', 'MaxFrequency', str(maxFreq))	#MaxFrequency
	config.set('CPU', 'MinFrequency', str(minFreq))	#MinFrequency

	config.write(open('logs/'+host+'_'+date+'.ini','w'))

	cprint ("************** CPU MODULE ********************", 'cyan', 'on_white')
	print "CPU Max Frequency: " + str(maxFreq)
	print "CPU min Frequency: " + str(minFreq)
	print "CPU Current Frequency: " + str(currentFreq)
	print "\n"

	# Envoi au server
	hote = "localhost"
	port = 15555

	mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	mysocket.connect((hote, port))
	#print "Connection on {}".format(port)

	mysocket.send("From " + host + "\n")

	mysocket.send("************** CPU MODULE ********************\n")
	mysocket.send("Current Frequency")
	mysocket.send(" : ")
	mysocket.send(str(currentFreq)+"\n")
	
	mysocket.send("Min Frequency")
	mysocket.send(" : ")
	mysocket.send(str(minFreq)+"\n")

	mysocket.send("Max Frequency")
	mysocket.send(" : ")
	mysocket.send(str(maxFreq)+"\n")
	
	mysocket.close()



def getHDD(date, host):

	config = ConfigParser.ConfigParser()
	config.read('logs/'+host+'_'+date+'.ini')

	# DISK USAGE PART
	hdd = psutil.disk_usage('/')

	total = str(hdd[0] / 1000000)
	used = str(hdd[1] / 1000000)
	free = str(hdd[2] / 1000000)
	percent = str(hdd[3])

	config.add_section('HDD')
	config.set('HDD', 'total', total)	#shared = 300
	config.set('HDD', 'used', used)	#buffers = 120
	config.set('HDD', 'free', free)
	config.set('HDD', 'percent', percent)

	config.write(open('logs/'+host+'_'+date+'.ini','w'))

	cprint ("************** HDD MODULE ********************", 'cyan', 'on_white')
	print "HDD total space " + str(total)
	print "HDD space available: " + str(free)
	print "HDD space used " + str(used)
	print "HDD space used in % " + str(percent)
	print "\n"

