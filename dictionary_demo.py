
def main():
    #the need for dictionarys 
    scores = [55, 75, 87, 82, 91]
    student = ["alice", "bob", "jerry", "jane", "bill"]
    #print the student name and score together
    for index in range(len(student)):
        print(f"{student[index]}: {scores[index]}")
        #using this kinda structure is not great because there is a lot that can go wrong therefore the use of the dictionary
    student_scores = { 
        "Alice": 55, 
        "Bob" : 75,
        "Jerry": 87,
        "Jane": 82,
        "Bill": 91
    }
    # the names act as "keys" meaning 
    # print bob and janes scores
    print(f" Bob's score {student_scores["Bob"]}")
    print(f" Jane's score :{student_scores["Jane"]}")
    #print all student data in the student scores dictionary
    print(":Get all student data")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")
    #create a car dictionary to store make, model, year value, engine size
    car_1 = {"make": "Ferrari", "model": "F-50", "year": 2021, "value": 500000, "engine": 4.8}
    #get all my car information
    print("\n get the car info")
    for key, value in car_1.items():
        print(f"{key}: {value}")
    car_2 = {"make": "Honda", "model": "Accord", "year": 2015,"value": 15000 }
    #create a list of dictionaries 
    dictionary_list = [car_1, car_2]
    print("\n display all car info")
    for car in dictionary_list:
        for feature, value in car.items():
            print(f"{feature}: {value}")
    #creat dictionary of dictionart 
    car_dictionary = {"Ferrari": car_1, "Honda":car_2}
    #write a for loop to displlay the car info
    #ferrari  
    #print all the ferari info
    # honda
    #print alll thge honda info
    for make, car in car_dictionary.items():
        print(f"Print info about {make}")
        for feature, value in car.items():
            print(f"{feature}: {value}")
main()
