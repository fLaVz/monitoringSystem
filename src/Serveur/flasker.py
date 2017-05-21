from flask import Flask
from flask import request



def writeInFile(data):

	path = data.partition(".ini")[0]
	print data

	F = open('serverLogs/'+path+'.ini','w')
	F.write(data)
	F.close()


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