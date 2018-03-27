#-*- coding: utf-8 -*-
import requests
import configparser

def sendRequest(date, host):

	file = open('logs/'+host+'_'+date+'.ini','r')
	line = host+'_'+date+'.ini\n'+file.read()			# met tout le contenu du fichier dans une variable + le nom du fichier qui doit etre crée
	file.close()

	Request = requests.post("http://localhost:5000/data", data=line)
	#print Request