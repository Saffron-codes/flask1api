import json
import sqlite3
from .user import User
#from ..models.user import User
conn = sqlite3.connect('database\database.sql',check_same_thread=False)
cur = conn.cursor()
def create_table():
    conn.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        PASSWORD CHAR(6) NOT NULL,
        NOTES BLOB  NOT NULL
        );''')
    print("Table created")
    return "Created"

def create_user(user):
    try:
        conn.execute('''
        INSERT INTO Users(NAME,PASSWORD,NOTES) \
            VALUES(?,?,?)
        ''',(user.Name,user.Password,user.notes))
        conn.commit()
        return login_user(user.Name,user.Password)
    except:
        return "Error occured creating user"


def get_all_user():
    users = []
    
    cur.execute("SELECT * FROM Users")
    rows = cur.fetchall()
    for i in rows:
        user = {}
        user["name"] = i[1]
        user["password"] = i[2]
        user["notes"] = i[3]
        users.append(user)
        print(i)
    return users
    # except:
    #     return "Error Occured"


def login_user(name,password):
    currentuser = {}
    try:   
        cur.execute("SELECT * FROM Users WHERE NAME=? AND PASSWORD=?",(name,password))
        rows = cur.fetchall()
        for i in rows:
            currentuser["name"] = i[1]
            currentuser["password"] = i[2]
            currentuser["notes"] = i[3]
        return currentuser
    except:
        return "Error Logging in "

def addnote(note,username):
    try:
        cur.execute("SELECT * FROM Users WHERE NAME=?",[username])
        rows = cur.fetchall()
        for i in rows:
            if i[3] == "":
                user_notes = note
            else:
                user_notes = str(i[3])+","+note
                print(user_notes)

        cur.execute("UPDATE Users SET NOTES = ? WHERE NAME = ?",(str(user_notes),username))
        conn.commit()
        return user_notes
    except:
        return "Error occured :("
