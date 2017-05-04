import re, urllib

def parse():

	htmlSource = urllib.urlopen("http://www.cert.ssi.gouv.fr/site/cert-fr_alerte.rss").read(20000)
	linksList = re.findall('<item><title>.*?</title>',htmlSource)
	lastAlert = linksList[0]
	lastAlert = lastAlert[13:-8]
	print lastAlert