import os

def getHostname():

	Host = os.popen('hostname')
	hostname = Host.readlines()
	hostname = hostname[0].strip()
	Host.close()
	return hostname
