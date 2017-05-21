from flask import Flask
from flask import request



def writeInFile(data):

	F = open('serverLogs/test.txt','w')
	F.write(request.data)
	F.close()



app = Flask(__name__)

@app.route('/')
def index():
    return "Hello !"

@app.route('/test', methods=['POST'])
def test():
	if request.method == 'POST':
		writeInFile(request.data)
		return "Msg received"


@app.route('/test', methods=['GET'])
def testd():
	if request.method == 'GET':
		myd = request.data
		return myd

if __name__ == '__main__':
    app.run(debug=True)



