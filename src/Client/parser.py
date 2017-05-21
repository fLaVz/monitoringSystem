import re, urllib
from termcolor import colored, cprint
import ConfigParser

def parse(date, host):

	cprint ("************** CERTALERT MODULE ********************", 'cyan', 'on_white')
	
	htmlSource = urllib.urlopen("http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss").read(20000)
	linksList = re.findall('<item><title>.*?</title>',htmlSource)
	lastAlert = linksList[0]
	lastAlert = lastAlert[13:-8]
	cprint (lastAlert, 'white', 'on_red')

	lastAlert = lastAlert.replace(" ", "_")

	config = ConfigParser.ConfigParser()
	config.read('logs/'+host+'_'+date+'.ini')

	config.add_section('ALERT')
	config.set('ALERT', 'CertAlert', lastAlert)
	config.write(open('logs/'+host+'_'+date+'.ini','w'))

	print "\n"