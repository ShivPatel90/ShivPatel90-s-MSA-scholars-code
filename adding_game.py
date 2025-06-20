import random




def get_level_inputs():
    while True:
        try: 
            level = int(input("Choose level of 1, 2, or 3"))
            if level >= 1 and level <= 3:
                break
        except:
            print("re enter level difficulty")
            continue
    return level

def get_question_number_input():
    while True:
        try:
            number_questions = int(input("Enter the number of questions "))
            if number_questions >=3 and number_questions<= 10:
                break
        except:
            print("re enter number of questions")
            continue
    return number_questions

def get_x_and_y(level):

    random_number_gen = random.Random()
    if level == 1:
        x = random_number_gen.randint(0,9)
        y = random_number_gen.randint(0,9)  
    elif level == 2:
        x = random_number_gen.randint(10,99)
        y = random_number_gen.randint(10,99)
    elif level == 3:
        x = random_number_gen.randint(100,999)
        y = random_number_gen.randint(100,999)
        
        
    return x, y


def main():
    level = get_level_inputs()
    number_questions = get_question_number_input()
    answered_correctly = 0
    #ask the user numberofquestions questions 
    for _ in range(number_questions):
        #generate x and y
        x, y = get_x_and_y(level)
        answer = x + y
        #prompt user with the question up to 3 times
        for number_of_tries in range(1, 4):
            
            try: 
                user_answer = int(input(f"{x} + {y} = "))

            except:
                print("WRONG!!!")
                if number_of_tries == 3:
                    print(f"{x} + {y} = {answer}")
                continue

            if user_answer == answer: 
                print("CORRECT!!!")
                answered_correctly += 1
                break
            else:
                print("WRONG!!!")
                if number_of_tries == 3:
                    print(f"{x} + {y} = {answer}")

                continue
    #add the x and y together and compare the value to the users input 
    #if they dont get it write in three trysthen consider it wrong
    #if they get it wrong they need to be reprompted
    #If they answered it correctly then add one to the number of questions answered correctly
    #divide the number of questions answered correctly by the number of questions
    success_percent = (answered_correctly / number_questions)* 100
    
    print(f"You got {answered_correctly} out of {number_questions} correct: {success_percent}%")

        

main()