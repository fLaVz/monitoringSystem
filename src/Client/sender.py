import requests
import ConfigParser
import json

def sendRequest(date, host):

	"""print 'logs/'+host+'_'+date+'.ini'


	config = ConfigParser.ConfigParser()
	config.read('logs/'+host+'_'+date+'.ini')

	cpuList = []
	hddList = []
	ramList = []
	
	cpuList.append(config.get('CPU', 'currentfrequency'))
	cpuList.append(config.get('CPU', 'maxfrequency'))
	cpuList.append(config.get('CPU', 'minfrequency'))

	ramList.append(config.get('RAM', 'total'))
	ramList.append(config.get('RAM', 'libre'))
	ramList.append(config.get('RAM', 'disponible'))

	hddList.append(config.get('HDD', 'total'))
	hddList.append(config.get('HDD', 'used'))
	hddList.append(config.get('HDD', 'free'))
	hddList.append(config.get('HDD', 'percent'))"""

	file = open('logs/'+host+'_'+date+'.ini','r')
	line = file.read()
	file.close()
	print line



	Request = requests.post("http://localhost:5000/test", data=line)
	print Request.text