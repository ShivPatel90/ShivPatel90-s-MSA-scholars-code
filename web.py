import flask 
from flask import request, jsonify
import student_generator_v2 as sg
#create a flaask app object
app = flask.Flask(__name__)
#tell the server to reload each time the code changes
app.config["DEBUG"] = True
#load student dictionaries
#create a route to display our name
@app.route('/', methods = ['GET'])
def index():
    return "<h1> My name is Shiv Patel</h1>"
#create a route to return all student data
@app.route('/api/students/all', methods=['GET'])
def api_all():
    #load student dictionaries
    student_dictionaries = sg.get_student_dictionaries()

    return jsonify(student_dictionaries)
#create a route to return students by major
@app.route('/api/majors/<string:major>', methods=['GET'])
def api_students_by_major(major):
    print(major)
    #get studentds with major
    #use for loop to search
    major_students = []
    student_dictionaries = sg.get_student_dictionaries()
    for student in student_dictionaries:
        if major.lower() == student['major'].lower():
            major_students.append(student)

    return jsonify(major_students)
# - return alll student data
# return students by major
#run the application
app.run()