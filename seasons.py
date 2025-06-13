

def get_season_name(month_number: int):
    if ((month_number == 12) or (month_number == 1) or (month_number == 2)):
        return "winter"
        
    elif ((month_number == 3) or (month_number == 4) or (month_number == 5)):
        return "spring"
       
    elif ((month_number == 6) or (month_number == 7) or (month_number == 8)):
        return "summer"
       
    elif ((month_number == 9) or (month_number == 10) or (month_number == 11)):
        return "fall"
    

def get_season_name_2(month_number: int):
    if month_number in [12, 1, 2]:
        return "winter"
        
    elif month_number in [3, 4, 5]:
        return "spring"
       
    elif month_number in [6, 7, 8]:
        return "summer"
       
    elif month_number in [9, 10, 11]:
        return "fall"   
        


def get_month_number():
    while True:
        try:
            month_number = int((input("What is the month number")))
            if month_number<= 0 or month_number> 12:
                print("ERROR: ENTER NUMBER IN RANGE 1-12")
                continue
            else:
                break
        except:
            print("ERROR ENTER REAL NUMBER")
            continue
    
    return month_number

   
    #validate the input si 1-12
    #reprompt user if input not valid

def main():
    
    #call the get_month number prompt and get the mont h number from the user 
    #call the get_season_name function to get the name of the season
    #print the output 
    #ask the user if they want to run the program again
    #if y or Y rerun the program, other wise end the program
    while True:
        month_number = get_month_number()
        season_name = get_season_name(month_number)
        print(season_name)
        re_enter = input("if you would like to run the program if yes press Y")
        if re_enter == "Y" or re_enter  == "y":
            continue
        else:
            break





main()