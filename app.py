from flask import Flask,redirect,url_for,render_template,request
from pymongo import MongoClient
import jwt
from datetime import datetime, timedelta
import hashlib
from werkzeug.utils import secure_filename

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/')
def Destinasi():
    return render_template('Destinasi.html')

if __name__ == '__main__':
  
   app.run('0.0.0.0', port=5000,debug=True)
