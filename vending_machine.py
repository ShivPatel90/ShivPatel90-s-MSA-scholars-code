
    
def get_user_input():
    #set up loop that will validate the input, 1 5 10 25 or if it is some random characters
    while True:
        try:
            amount_entered = int(input("\n INSERT COIN: \n "))
            if amount_entered in [1, 5, 10, 25]:
                break
            else:
                print("Renter: Numbers 1 5 10 25")
                continue

        except: 
            print("ERROR: Number 1 5 10 25")
    return amount_entered
    #prompt user and validate input for how much is taken off
    # the variable will need to be changed everytime there is a new input

def calculate_amount_due(amount_entered, amount_due):
    amount_due = amount_due - amount_entered
    return amount_due
    #calculate the amount that is still due after a coin is put in

def main( ):
    amount_due = 50
    while True:
        print(f"\n AMOUNT DUE:{amount_due}")
        #if the amount due is greater than 0 then it will continue the loop however if not then it will break and end the prgram
        amount_entered = get_user_input()
        amount_due = calculate_amount_due(amount_entered, amount_due)
        
        #print vending machine
        print(f"RUN VENDING MACHINE\n___________________")
        #user input function to get user input
        
        if amount_due > 0:
            continue
        else:
            break
    amount_owed = amount_due * -1
    print(f"YOUR CHANGE: {amount_owed}")    
    

main()