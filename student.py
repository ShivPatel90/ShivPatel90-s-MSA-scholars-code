class Student():
    def __init__(self, first_name, last_name, major, credit_hours, gpa, student_id):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__student_id = student_id
    
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name
    def get_major(self):
        return self.__major
    def set_major_name(self, new_major):
        self.__major = new_major
    def get_credit_hours(self):
        #you can change this so you will need a getter and a setter
        return self.__credit_hours
    def set_credit_hours(self, new_credit_hours: int):
        self.__credit_hours = new_credit_hours
    def get_gpa(self):
        #No calculations needed for the GPA
        return self.__gpa
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa
    def get_student_id(self):
        #this will remain constant so only a get
        return self.__student_id
    
    def get_class_level(self):
        if self.__credit_hours <= 30 and self.__credit_hours >= 0:
            return "freshman"
        elif self.__credit_hours <= 60 and self.__credit_hours >= 31:
            return "sophmore"
        elif self.__credit_hours <= 90 and self.__credit_hours >= 61:
            return "junior"
        elif self.__credit_hours >= 90:
            return "senior"
    
    def update_credit_hours(self, additional_hours):
        self.__credit_hours += additional_hours
        
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}\nClass level: {self.get_class_level()}\nMajor: {self.__major}")
        print(f"GPA: {self.__gpa} ID: {self.__student_id}\n")