from flask import Flask
import pymongo
import secret

app = Flask(__name__)


# Define a new client.



client = pymongo.MongoClient("mongodb+srv://" + secret.username + ":"+ secret.password +"@cluster0.eicqs8o.mongodb.net/?retryWrites=true&w=majority")

db = client.test

mydb = client["wizard"]
print(str(mydb))
print("")

print("")

print("")

print("")
print(mydb.list_collection_names())


@app.route('/hi')
def hello():
	return "Hello tom"
	
@app.route('/')
def data():
	return "hi"

app.run(host='0.0.0.0', port=81)
