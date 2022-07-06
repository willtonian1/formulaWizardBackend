from flask import Flask, request, jsonify
import pymongo
import secret
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

app.run(debug=True)

# Define a new client.
client = pymongo.MongoClient("mongodb+srv://" + secret.username + ":"+ secret.password +"@cluster0.eicqs8o.mongodb.net/?retryWrites=true&w=majority")

db = client.test

mydb = client["wizard"]
print(str(mydb))
mycol = mydb["cars"]


def getDB():
	
	list = []

	cursor = mycol.find({})

	for document in cursor:
		print(document)
		print("")
		list.append(document)
	return str(list)


@app.route('/')
def data():
	return getDB()



@app.route('/', methods=['POST'])
def add_articles():
	name = request.json
    
	print(str(name))
  #db.session.add(article)
  #db.session.commit()
	mycol.insert_one(name)

	
	getDB()
	data()
	return 
	#jsonify(article)
	

app.run(host='0.0.0.0', port=81)
