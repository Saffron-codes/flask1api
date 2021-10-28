import os
from flask import Flask,request
import json

from flask.helpers import send_from_directory
from  auth import login_user,create_table,get_all_user,create_user,addnote
from  user import User
app = Flask(__name__)



@app.route("/")
@app.route("/favicon.ico")
def homepage():
    return "Welcome to API for flutter"


@app.route('/login',methods=['GET'])
def home():
    name = request.args['name']
    password = request.args["pass"]
    user = login_user(name,password)
    return json.dumps(user,indent=4)

@app.route('/create',methods=['GET'])
def createuser():
    create_table()
    name = request.args['name']
    password = request.args["pass"]
    created_user = create_user(User(name,password,""))
    return json.dumps(created_user,indent=4)

@app.route('/users')
def get_users():
   users = get_all_user()
   return json.dumps(users,indent=4)


@app.route('/add',methods=['GET'])
def add_note():
    note = request.args["note"]
    name = request.args["name"]
    output = addnote(note,name)
    return json.dumps(output,indent=4)


if __name__ == "__main__":
    app.run(debug=True)