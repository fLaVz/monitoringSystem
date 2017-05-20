import psutil
import configparser

def getCPU(date, host):

	#config = ConfigParser.ConfigParser()
	#config.read(host+'_'+date+'.ini')


	# CPU PART
	freq = psutil.cpu_freq()
	currentFreq = freq[0]
	maxFreq = freq[1]
	minFreq = freq[2]

	config.add_section('CPU')
	config.set('CPU', 'CurrentFrequency', str(currentFreq))	#CurrentFrequency
	config.set('CPU', 'MaxFrequency', str(maxFreq))	#MaxFrequency
	config.set('CPU', 'MinFrequency', str(minFreq))	#MinFrequency

	config.write(open(host+'_'+date+'.ini','w'))

def getHDD(date, host):

	config = ConfigParser.ConfigParser()
	config.read(host+'_'+date+'.ini')

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

	config.write(open(host+'_'+date+'.ini','w'))

