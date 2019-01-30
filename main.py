from flask import Flask, render_template
import os
#from data import Articles
from flask_pymongo import PyMongo


wallet = Flask (__name__)
wallet.config["MONGO_URI"] = "mongodb://localhost:27017/userdata"

mongo=PyMongo(wallet)
#Articles=Articles()
#mongo.db.createCollection('userdata')


@wallet.route('/')
def home():
	return render_template('home.html')

@wallet.route('/contact')
def contact():
	return render_template('contact.html')

@wallet.route('/articles')
def articles():
	return render_template('articles.html', articles=Articles)

@wallet.route('/enter')
def enter():
	user= mongo.db.userdata
	user.insert_one({'name' : 'Soumya'})
	return 'Added User!'

@wallet.route('/welcome')
def welcome(): 
	return render_template('welcomepage.html')

if __name__== ('__main__'):
	wallet.run(debug=True)