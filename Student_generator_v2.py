from datetime import datetime
from Student import Student
"""
Function to write an errror message to a log file
input: string error m,essage
output:none
"""
def write_to_error_log(message:str) -> None:
    error_log = open("error_log.txt", "a")
    #open the log file in append mode: error_log.txt
    the_date = datetime.now()
    with open("error_log.txt", "a") as file:
        file.write(f"{the_date}: {message}\n")
    #write error message to the file in the format
    #date: message -> 6/24/2025: error in datafile on line 5
    #close file 
    return
"""
Function to return a list of student objects
Input: none
output: list of student objects
"""

def load_students():
    #open file.txt
    data_file = open("students.csv", "r")
    #create an empty dictionary to store item: price
    student_data = []
    
    #use a loop to read the contents of a file line by line
    line_number = 0
    for line_of_data in data_file:
        line_number += 1 
        students_and_data = line_of_data.split(",")
        if len(students_and_data) != 6:
            message = f"ERROR: Incorret data format on line: {line_number}"
            write_to_error_log(message)
            continue
        
        first_name = students_and_data[0]
        last_name = students_and_data[1]
        major = students_and_data[2]
        student_id = students_and_data[5]
        try:
            credit_hours = int(students_and_data[3])
            gpa = float(students_and_data[4]) 
        except:
            message = f"ERROR: Conversion issue on line: {line_number}"
            write_to_error_log(message)
            continue

        the_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        student_data.append(the_student)

    data_file.close()
    return student_data



"""
function to convert student objectgs to sutdent dictionaries
input: list of student objects
output: list of student dictionaries
"""
def student_to_dictionaries(list_of_students: list[Student]) -> list[dict]:
    #create a list to store the dicts in
    student_dictionary_list = []
    #loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dictionary 
        student_dictionary = {}
        #set the keys and value
        student_dictionary["first_name"] = student.get_first_name()
        student_dictionary["last_name"] = student.get_last_name()
        student_dictionary["major"] = student.get_major()
        student_dictionary["gpa"] = student.get_gpa()
        student_dictionary["class"] = student.get_class_level()
        student_dictionary["id"] = student.get_student_id()
        student_dictionary_list.append(student_dictionary)
        #append the dictionary to the list of dictionaries
    # return the list of dictionaries
    return student_dictionary_list


"""
function to get a list of students dictionary
input none
outpuyt: list of student dictionaries
"""

def get_student_dictionaries():
    #get a list of students
    #get list of student dictionaries
    student_dictionaries = student_to_dictionaries(student_list)
    print(student_dictionaries)
    return student_dictionaries
    
get_student_dictionaries()