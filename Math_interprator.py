
def main(): 
    while True:
        #get user input
        xyz_input = input("Enter input in this form: X Y Z ")
        #use the split method to get the parts of the expression
        xyz_list = xyz_input.split(" ")
        
            
            #check the legth of the  list returned from .split
            #if len(list) not = 3, then output incorrect format message reprompt continue
            #try
            #try
            #get x and y and z vakyes from the list and check if X and z are integers bby converting to int()
            #except
            #output error message and repprompt continue
        if not len(xyz_list) == 3:
            continue
        
        try:
            x = int(xyz_list[0])
            y = xyz_list[1]
            z = int(xyz_list[2])
            
        except:
            print("Re enter values")
            continue

        if (y != '+' and  y != '-' and y != '*' and y != '/'):
            print("EEROR")
            continue

        if y == '+':
            output = x + z
            print(F" {x} + {z} = {output}")
        elif y == '-':
            output = x - z 
            print(F" {x} - {z} = {output}")
        elif y == '*':
            output = x * z 
            print(F" {x} * {z} = {output}")
        elif y == '/':
            if z == 0:
                print("z cannot equal zero")
                continue 
            output = x / z 
            print(F" {x} / {z} = {output}")

        
        break


        
    
    #check that operator is +, -, *, /
    #if operator is not in some list of operators then output some error message and reprompt some user (continue)
    #determine the operation to carry out based on the value of the operator
    #use if/ekif/else bock ot evaluate the operator and carry out the appropriate the operatore
main()
