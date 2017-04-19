import re, urllib
htmlSource = urllib.urlopen("http://dominique.frin.free.fr/").read(200000)
linksList = re.findall('<a href=(.*?)>.*?</a>',htmlSource)
for link in linksList:
    print link