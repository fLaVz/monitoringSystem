#-*- coding: utf-8 -*-
# Récupérer une sortie de commande pour la stocker dans un format de donnée donné

import os
import ConfigParser

config = ConfigParser.ConfigParser()
S = '1'
config.read('rapport'+S+'.ini')

os.system("free -m")
RAM = os.popen('free -m')

message = RAM.readlines()
RAM.close()

Buff = message[0].split('    ')
Buff2 = message[1].split('    ')

config.add_section('RAM')
config.set('RAM', Buff[3].replace(" ",""), Buff2[2].replace(" ",""))	#total = 3833
config.set('RAM', Buff[4].replace(" ",""), Buff2[3].replace(" ",""))	#used = 2453
config.set('RAM', Buff[5].replace(" ",""), Buff2[4].replace(" ",""))	#free = 1380
config.set('RAM', Buff[6].replace(" ",""), Buff2[6].replace(" ",""))	#shared = 300
config.set('RAM', Buff[7].replace(" ",""), Buff2[8].replace(" ",""))	#buffers = 120
config.set('RAM', Buff[8].replace(" ","").replace("\n",""), Buff2[9].replace(" ","").replace("\n",""))	#cached = 1252
config.write(open('rapport1.ini','w'))


#TODO après avoir récupérer les infos il faut les écrire sous la bonne forme dans un fichier .ini
