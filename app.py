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
    student_data = get_student_data(url)
    print(student_data)
    return render_template("index.html", student_data = student_data)
#create a route for the majors search page wtih get request
@app.route('/majors', methods =['GET'])
def majors_get():
    # get a list of student data
    url = 'http://127.0.0.1:5000/api/students/all'
    student_data = get_student_data(url)
    #create a list to store unique majors
    major_list = []
    #use for loop to iterate through the student list
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])
        
        major_list.sort()
        #get the form data

    return render_template('majors.html', major_list = major_list)

@app.route('/majors', methods =['POST'])
def majors_post():
    # get a list of student data
    url = 'http://127.0.0.1:5000/api/students/all'
    student_data = get_student_data(url)
    #create a list to store unique majors
    major_list = []
    #use for loop to iterate through the student list
    for student in student_data:
        if student['major'] not in major_list:
            major_list.append(student['major'])
        
        major_list.sort()
        #get the fortm data: chosen major
    major = request.form.get('major').strip()
    print(f"Major: {major}")
    url =f"http://127.0.0.1:5000/api/majors/{major}"
    result_list = get_student_data(url)
        #create the request url to get students with that major
        # send the request and get the request
        #send the results to the majors template
    return render_template('majors.html',  major_list=major_list, result_list=result_list)
