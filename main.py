import os
from flask import Flask,request,jsonify
import json

from flask.helpers import send_from_directory
from  app.auth import login_user,create_table,get_all_user,create_user,addnote
from  app.user import User
app = Flask(__name__)



@app.route("/")
def homepage():
    return "Welcome to API for flutter"


@app.route('/login',methods=['GET'])
def home():
    name = request.args['name']
    password = request.args["pass"]
    user = login_user(name,password)
    return jsonify(user)

@app.route('/create',methods=['GET'])
def createuser():
    create_table()
    name = request.args['name']
    password = request.args["pass"]
    created_user = create_user(User(name,password,""))
    return jsonify(created_user)

@app.route('/users')
def get_users():
   users = get_all_user()
   return jsonify(users)


@app.route('/add',methods=['GET'])
def add_note():
    note = request.args["note"]
    name = request.args["name"]
    output = addnote(note,name)
    return jsonify(output)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 
        'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)