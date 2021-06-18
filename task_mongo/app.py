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

# for POST --> request.form.get()
# for GET --> request.args.get()
@app.route("/adddata", methods=['POST'])  
def add_data():
    if request.method == 'POST':
        userid = request.form.get("a")
        name = request.form.get("x")   
        age = request.form.get("y")
        loc = request.form.get("z")
        if userid != "" and name != "" and age != "" and loc != "":
            user = user_collection.insert_one({"userid": userid,"name": name, "age": age, "location": loc})
            return ("data added to the database")
        else:
            return ("Kindly fill the form")

@app.route("/display")
def read_data():
    user = (user_collection.find())
    return render_template('display.html', user=user)

@app.route("/delete", methods=['POST'])
def delete_data():
    return render_template('delete.html')

@app.route("/remove",methods=['POST'])
def delete():
    if request.method == 'POST':
        userid = request.form.get("a")
        if userid != "":
            user= user_collection.delete_one({"userid": userid})
            return "Record deleted"
        else:
            return "Kindly Enter ID"
            
app.run(port=5555,debug=True)
