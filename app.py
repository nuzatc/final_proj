# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo
import os 
import requests 

# from flask_pymongo import PyMongo
# -- Initialization section --
app = Flask(__name__)
# name of database
app.config['MONGO_DBNAME'] = 'final_proj'
# URI of database
user = os.environ["user"]
pw = os.environ["pw"]
app.config['MONGO_URI'] = f'mongodb+srv://{user}:{pw}@cluster0.vuqlg.mongodb.net/final_proj?retryWrites=true&w=majority'
mongo = PyMongo(app)
hor = mongo.db.hor
senate = mongo.db.senate
gov = mongo.db.gov
mayor = mongo.db.mayor
# -- Routes section --
# INDEX
 # --- HOMEPAGE WITH A FORM TO SUBMIT A ZIPCODE
@app.route('/')
@app.route('/index')
def index():
    #step1 connect to database
    hor1 = mongo.db.hor
    senate1 = mongo.db.senate
    gov1 = mongo.db.gov
    #step2 do a query for all events in db
    hors = list(hor1.find({}))
    senates = list(senate1.find({}))
    govs = list(gov1.find({}))
    print(hors)
    print(senates)
    print(govs)

    #step3 return render template
    return render_template('index.html', hors = hors, senates = senates, govs = govs)

@app.route('/yourRepresentatives', methods = ["GET", "POST"])
def yourRepresentatives():
    if request.method == "POST":
        #RENDER TEMPLATE 
        #1 get data from form
        user_district = request.form["district"]
        #2 print data
        print(user_district)
        #2.5 connect database 
        hor1 = mongo.db.hor
        senate1 = mongo.db.senate
        gov1 = mongo.db.gov
        #3 query mongo zipcodes that match user input
        horss = list(hor1.find({"district": user_district}))[0]
        senatess = list(senate1.find({}))[0]
        senatesss = list(senate1.find({}))[1]
        govss = list(gov1.find({}))[0]
        print(horss)
        print(senatess)
        print(govss)
        #4 print mongo query
        return render_template('yourRepresentatives.html', horss = horss, senatess = senatess, govss = govss, senatesss = senatesss)
    else:
        return "hello hello"

@app.route('/YourRepresentatives/<collection>/<politician>' , methods = ["GET", 'POST'])
def politicianPage(collection, politician):
    # user_district = request.form["district"]
    if collection == "hor":
        poli1 = mongo.db.hor
        poli = list(poli1.find({"name": politician}))[0]
        print(poli)
        return render_template('SpecificRepresentative.html', poli = poli)
    elif collection == "senate":
        poli1 = mongo.db.senate
        poli = list(poli1.find({"name": politician}))[0]
        print(poli)
        return render_template('SpecificRepresentative.html', poli = poli)
    elif collection == "gov":
        poli1 = mongo.db.gov
        poli = list(poli1.find({"name": politician}))[0]
        print(poli)
        return render_template('SpecificRepresentative.html', poli = poli)
# CONNECT TO DB, ADD DATA
# @app.route('/add')
# def add():
#     # connect to the database
#     # insert new data
#     # return a message to the user
#     return ""




@app.route('/yourgif', methods = ["GET", "POST"])
def yourgif():
    # need to store user import 
    user_data= request.form["gifchoice"]
    print (user_data)
    link = getImageUrlFrom(user_data)
    return render_template('yourgif.html', link=link)