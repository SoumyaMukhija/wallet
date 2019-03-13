from flask import Flask, render_template, request, flash, session 
import os
from tkinter import messagebox as mb
#from data import Articles
from flask_pymongo import PyMongo
import bcrypt #hashes/encrypts your password 


wallet = Flask (__name__)

wallet.config["MONGO_DBNAME"]='userdata' #Name of the database
wallet.config["MONGO_URI"] = "mongodb://localhost:27017/userdata"

mongo=PyMongo(wallet)
user= mongo.db.userdata #userdata is a collection assigned to the variable user

#Articles=Articles()
#mongo.db.createCollection('userdata')


@wallet.route('/') #creates a route or a path
def home():
	if 'username' in session:
		return 'You are logged in as ' + session['username']
	return render_template('index.html')

'''@wallet.route('/contact')
def contact():
	return render_template('contact.html')'''

@wallet.route('/enter', methods=['POST'])
def enter():
	pre_existing = user.find_one({'name': request.form['username']}) #welcomepage form name = username, check for redundancy 
	if pre_existing is not None:									#pre-existing user
		return render_template('login.html', name= pre_existing)
	else:
		name=request.form['username']
		return render_template('register.html', name=name)

@wallet.route('/register')
def register(name):
	hashpass=bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.genSalt()) 
	contactnumber=request.form['contactnumber']
	confirmpassword=request.form['confirmpassword']
	if confirmpassword != request.form['password']:
		mb.showerror('The passwords did not match. Please try again.')
	else:
		user.insert({'name' : name, 'password' : hashpass, 'contact' : contactnumber}) #stores the hashed version of the password, increases security
		session['username']=request.form['username'] 
		return render_template('login.html', name=name)


@wallet.route('/<name>')
def login(name):
	return 'hI!'



'''@wallet.route('/newuser', methods=['GET'])
def newuser():
	password=request.form['password']
	user=mongo.db.userdata
	username=request.form['username
	user.update( {'name':username}, {'$set': {'name':username, 'password':password} } )
	return render_template('confirmpassword.html')



	@wallet.route('/confirmpassword', methods=['GET'])
def confirmpassword(): 
	username=request.form('username')
	password=request.form('password')
	confirm=request.form('confirmpassword')
	user=mongo.db.userdata
	if confirm==password:
		return render_template('pre_existing.html')
	else:
		flash('Whoops! The passwords did not match. Please try again.')
		return render_template('confirmpassword.html')



@wallet.route('/<pre_existing>')
def mainpage(pre_existing): 
	return render_template('pre_existing.html', name=pre_existing)'''


if __name__== ('__main__'):
	wallet.run(debug=True)