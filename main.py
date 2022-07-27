from flask import Flask, request, jsonify
import pymongo
import secret
#from flask_cors import CORS
import json
import ast

app = Flask(__name__)

#CORS(app)

# Define a new client.
client = pymongo.MongoClient(
    "mongodb+srv://" + secret.username + ":" + secret.password +
    "@cluster0.eicqs8o.mongodb.net/?retryWrites=true&w=majority")

db = client.test

mydb = client["wizard"]
#print(str(mydb))
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
	#
		getDB()
		return data()

    #jsonify(article)

@app.route("/vote")
def vote_Screen():
	return "hi"

@app.route("/leaderboard")
def board():
		names_list = []
		docs = list(mycol.find())
		for doc in docs:

				a = str(doc['name'])
				b = int(doc['votes'])
			
				names_list.append([a,b])

		for i in range(len(names_list)):
        # We want the last pair of adjacent elements to be (n-2, n-1)
				for j in range(len(names_list) - 1):
						if names_list[j][1] > names_list[j+1][1]:
            # Swap
									names_list[j], names_list[j+1] = names_list[j+1], names_list[j]

		final_j_string = ''
		for item in range(len(names_list)):
				j = { "name": names_list[item][0] , "votes" : names_list[item][1] }
				final_j_string = final_j_string + (str(j))

		final_j_string = '[' + final_j_string
		final_j_string = final_j_string + ']'

		return final_j_string




	
@app.route("/vote", methods=["POST"])
def vote():
	
	name_val = (request.json)
	a = (str(name_val))
		 
	#n = a.replace(a[10] , '')
	print(a)


	y = ast.literal_eval(a)
	x = mycol.find_one(y,{'_id':0,'votes':1})
	
	oldV = int(x['votes'])
	newV = oldV + 1
	print(newV)
	mycol.update_one(y,  {"$set" : {"votes" : str(newV)}})

	
	return ''
app.run(debug=True, use_reloader=True ,host='0.0.0.0', port=8080)

	
