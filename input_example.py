# write a pound to kilogram conversion program
# A user will be prompted for the weight in pounds and the program will output the weight in kilograms
# get user's weight input
def get_positive_float_input():
    while True:
        try:
            user_lb_weight = float(input("What is your weight in pounds"))
            #validate that user weight is posistive, if it is negative then reprompt user until correct
            if user_lb_weight <= 0:
                print("Error: please enter number greater than zero")
                continue
            else:
                break
        except:
            print("Error: please enter a number")
    return user_lb_weight
def main():
    # get the weight from the user call the get positive float function
    user_lb_weight = get_positive_float_input()
    #if weight isnt a nnumber then reprompt them until they change it
    # processing: use a conversion to convert lbs to kgs 2.205 lbs = 1 kilo
    LB_KG_CONVERSION = 2.205
    user_kg_weight = user_lb_weight / LB_KG_CONVERSION
    #output, print the otuput to user with good format rounding to 2 decimal places 
    user_kg_weight_rounded = round(user_kg_weight, 2)
    print(f"The conversion is {float(user_kg_weight_rounded)} kgs")
#calling main function
main()
