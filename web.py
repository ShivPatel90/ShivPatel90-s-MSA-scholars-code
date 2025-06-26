import flask 
from flask import request, jsonify
import student_generator_v2 as sg
#create a flaask app object
app = flask.Flask(__name__)
#tell the server to reload each time the code changes
app.config["DEBUG"] = True
"""
function to query student dictionaries based on search key
input: search key
output: a list of results
"""
def search_student_data(search_value, search_key):
    
    student_dictionaries = sg.get_student_dictionaries()
    list_results = []
    
    for student in student_dictionaries:
        if search_value.lower() == student[search_key].lower():
            list_results.append(student)
    return list_results
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
    major_students = search_student_data(major, "major")

    return jsonify(major_students)
#create a route to return a student based on an ID url parameter
@app.route('/api/students/<string:id>', methods = ['GET'])
def api_students_id(id):
    print(id)
    student_dictionaries = sg.get_student_dictionaries()
    target_student = None
    #search student dictionaries based on ID
    for student in student_dictionaries:
        if student['id'] == id:
            target_student = student
            break
    return jsonify(target_student)
@app.route('/api/student/class/<string:class_rank>', methods = ["GET"])
def api_students_class_rank(class_rank):
    student_class = search_student_data(class_rank, 'class')
    return jsonify(student_class)
# - return alll student data
# return students by major
#run the application
app.run()