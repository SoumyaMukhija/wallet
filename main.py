from flask import Flask, render_template
import os


pocket = Flask (__name__)

@pocket.route('/')
def home():
	return render_template('home.html')

@pocket.route('/about')
def about():
	return render_template('about.html')

@pocket.route('/contact')
def contact():
	return render_template('contact.html')


if __name__== ('__main__'):
	pocket.run(debug=True)