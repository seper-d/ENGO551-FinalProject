import os
import csv 
import json 
import requests

from flask import Flask, session, render_template, request, jsonify 
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

engine = create_engine(os.getenv("DATABASE_URL")) 
db = scoped_session(sessionmaker(bind=engine)) 


@app.route("/") 
def index():
    if 'user' in session: 
        username = session['user']
        return render_template("index.html", username = username) 

    return render_template("signin.html") 

@app.route("/signin") 
def signin():

    return render_template("signin.html") 

@app.route("/signincheck", methods=["POST"]) 
def signincheck():
    username = request.form.get("username_old")
    password = request.form.get("password_old")

    checkuser = db.execute("SELECT * FROM userlog WHERE (username = '{username}') AND (password = '{password}')".format(username = username, password = password)).fetchone()

    if checkuser is None:
        return render_template("failed.html", username = username, password = password)
    session["user"] = username
    return render_template("index.html", username = username, password = password)

@app.route("/signup")
def signup():

    return render_template("signup.html")

@app.route("/signupcheck", methods=["POST"])
def signupcheck():
    username = request.form.get("username_new")
    password = request.form.get("password_new")

    checkuser = db.execute("SELECT * FROM userlog WHERE (username = '{username}')".format(username = username)).fetchone()

    if checkuser is None:
        db.execute("INSERT INTO userlog (username, password) VALUES (:username, :password)",{"username":username, "password":password})
        db.commit()
        session["user"] = username
        return render_template("signin.html", username = username, password = password)
    return render_template("signupfail.html", username = username, password = password)

@app.route("/logout") 
def logout():

    return render_template("signin.html") 
