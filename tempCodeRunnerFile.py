
import json
from flask import Flask, render_template, request
import re
from flask_sqlalchemy import SQLAlchemy

with open('templates/config.json','r') as c:
    data=json.load(c)
    params=data["params"]

app = Flask(__name__ , static_url_path='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = params["local_uri"]
db = SQLAlchemy(app)

class Hire_me(db.Model):
    '''
    sno, name email, msg
    '''
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(20), nullable=False)
    msg = db.Column(db.String(120), nullable=False)

@app.route('/')
def index():
    return render_template('index.html',params=params)

@app.route('/resume')
def resume():
    return render_template('resume.html' ,params=params)

@app.route('/projects')
def projects():
    return render_template('projects.html',params=params)

@app.route('/Hire', methods = ['GET', 'POST'])
def Hire():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('msg')
        phone=request.form.get('phone')
        subject=request.form.grt('subject')
        entry = Hire_me(name=name, email = email,phone=phone,subject=subject, msg = message)
        db.session.add(entry)
        db.session.commit()
    return render_template('Hire_Me.html',params=params)

if __name__ == '__main__':
    app.run(debug=True)
