from flask import Flask, render_template, request
from flask_pymongo import PyMongo

#initialize the Flask app
app = Flask("myapp")
#connect and create a db named as mydb
app.config["MONGO_URI"] = "mongodb://127.0.0.1:27017/mydb"
#initializing the client for mongodb
dbmongo = PyMongo(app)
#creating the user collection(
user_collection = dbmongo.db.users

@app.route("/userform")
def userform():
   return render_template('user.html')
   
@app.route("/adddata", methods=['POST'])  #GET --->POST
def add_data():
    if request.method == 'POST':
        name = request.form.get("x")   #args--->form
        age = request.form.get("y")
        loc = request.form.get("z")
        if name != "" and age != "" and loc != "":
            user = user_collection.insert_one({"name": name, "age": age, "location": loc})
            return ("data added to the database")
        else:
            return ("Kindly fill the form")

@app.route("/display")
def read_data():
    user = (user_collection.find())
    return render_template('display.html', user=user)

@app.route("/delete")
def delete_data():
    return render_template('delete.html')

@app.route("/remove",methods=['POST'])
def delete():
    if request.method == 'POST':
        name = request.form.get("x")
        if name != "":
            user= user_collection.delete_one({"name": name})
            return "Record deleted"
        else:
            return "Kindly Enter Name"
            
app.run(port=5555,debug=True)