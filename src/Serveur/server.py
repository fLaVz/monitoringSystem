import requests


mydata="jeusis1test"

r = requests.get("http://localhost:5000/test", data=mydata)
print r.text