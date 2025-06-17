def get_valid_expression_inputs():
    while True:
        xyz_input = input("Enter input in this form: X Y Z ")
        xyz_list = xyz_input.split(" ")
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
            print("ERROR")
            continue
        else: 
            break
    return x, y, z
    """function to eval an expression 
    inputs: x(int) y(str) z(int)
    outputs: answer
    """
def evaluate_expression(x, y, z):
    
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
                print("Invalid expression: re enter inputs")
                main()
            output = x / z 

            print(F" {x} / {z} = {output}")

def main():
    xyz_list = get_valid_expression_inputs()
    x = int(xyz_list[0])
    y = xyz_list[1]
    z = int(xyz_list[2])
    evaluate_expression(x, y, z)
    #call the get valid expression inputs function to get x y z
    # call the eval expression to get the answert for the expression
    #print the answer
    #ask the user if they want to eval another expression
    #rerun the program if the user wants to continue, otherwise end the program
main()