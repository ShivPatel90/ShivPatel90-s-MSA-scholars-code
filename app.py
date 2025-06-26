from flask import Flask, render_template, request, url_for, redirect, abort, flash
import requests
#make a flask app 
app = Flask(__name__)
app.config["DEBUG"] = True
#Set a secret key
app.config['SECRET_KEY'] = 'your secret key'

"""
function to request student data from the api
input url
output json
"""
def get_student_data(url):
    #make a request
    response = requests.get(url)
    #convert response format to JSON
    response_json = response.json()
    return response_json
#create a route for the website index/roo. will display all
@app.route('/', methods =['GET'] )
def index():
    url = 'http://127.0.0.1:5000/api/students/all'
    student_dat = get_student_data(url)
    return render_template("index.html")

app.run(port=5001)