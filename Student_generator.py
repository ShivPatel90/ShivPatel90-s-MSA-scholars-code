from Student import Student
def main():
    #open file.txt
    data_file = open("students.csv", "r")
    #create an empty dictionary to store item: price
    student_data = []
    #use a loop to read the contents of a file line by line
    for line_of_data in data_file:
        students_and_data = line_of_data.split(",")
        if len(students_and_data) != 6:
            continue
        
        first_name = students_and_data[0]
        last_name = students_and_data[1]
        major = students_and_data[2]
        student_id = students_and_data[5]
        try:
            credit_hours = int(students_and_data[3])
            gpa = float(students_and_data[4]) 
        except:
            continue

        the_student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        student_data.append(the_student)

    data_file.close()

    for student in student_data:
        student.print_student_data()
main()