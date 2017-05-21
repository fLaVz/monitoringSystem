#-*- coding: utf-8 -*-
from flask import Flask
from flask import request
import os



def writeInFile(data):

	path = data.partition(".ini")[0]
	hostname = path.partition("_")[0]

	if os.path.exists('serverLogs/'+hostname+'/') == False:		# Pour ranger par machine les fichers de configuration, crée un dossier dynamiquement
		os.mkdir('serverLogs/'+hostname+'/')
	else:
		print "Folder already exists; files stored in it"

	F = open('serverLogs/'+hostname+'/'+path+'.ini','w')
	F.write(data)
	F.close()
	print data


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

@app.route('/data', methods=['POST'])			# gere les methodes post et les traites grace a la fonction writeInFile
def test():
	if request.method == 'POST':
		writeInFile(request.data)
		return "Msg received"


@app.route('/data', methods=['GET'])			# gere les methodes get
def testd():
	if request.method == 'GET':
		myd = request.data
		return myd

if __name__ == '__main__':
    app.run(debug=True)