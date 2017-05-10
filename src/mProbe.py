#-*- coding: utf-8 -*-
# Récupérer une sortie de commande pour la stocker dans un format de donnée donné

import os
import ConfigParser


def getRAM(date, host):

	config = ConfigParser.ConfigParser()
	config.read(host+'_'+date+'.ini')

	os.system("free -m")
	RAM = os.popen('free -m')

	message = RAM.readlines()
	RAM.close()

	nbList = []
	keyList = []

	# Enleve les \n
	message[0] = message[0].strip()
	message[1] = message[1].strip()
	
	# Sépare par chaque espace
	Buff = message[0].split(' ')
	Buff2 = message[1].split(' ')
	
	# Test si ce ne sont que des chaines de  caracatere sans espace
	for i in Buff:
		if i.isalpha():
			keyList.append(i)

	# Teste si c'est une chaine de nombre
	for i in Buff2:
		if i.isdigit():
			nbList.append(i)

	# Ecrit dans le fichier
	config.add_section('PC: '+host)
	config.add_section('RAM')
	config.set('RAM', keyList[0], nbList[0])	#total = 3833
	config.set('RAM', keyList[1], nbList[1])	#used = 2453
	config.set('RAM', keyList[2], nbList[2])	#free = 1380
	config.set('RAM', keyList[3], nbList[3])	#shared = 300
	config.set('RAM', keyList[4], nbList[4])	#buffers = 120
	config.set('RAM', keyList[5], nbList[5])
	config.write(open(host+'_'+date+'.ini','w'))

	print nbList
	print keyList
	#print message[1].replace(" ","/")
#TODO après avoir récupérer les infos il faut les écrire sous la bonne forme dans un fichier .ini
