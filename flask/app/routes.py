from app import app
from flask import render_template
from app.scraper import parse

@app.route('/')
@app.route('/index')
def index():
	user = {'username':'CAEN'}
	posts = [
		{
			'author':{'username':'Mark Schlissel'},
			'body':'Beautiful day in Michigan'	
		},
		{
			'author':{'username':'Alec Gallimore'},
			'body':'Beautiful day in the College of Engineering'
		}
	]
	return render_template('index.html',title='Home',user=user,posts=posts)	

@app.route('/software')
def software():
	data = parse()
	return render_template('mytable.html',rows = data[0],headers=data[1])
