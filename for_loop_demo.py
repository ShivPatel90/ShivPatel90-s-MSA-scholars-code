# this file will demo how for loops will work

def main():
    #print integers between 0 and 10
    print("output numbers between 0 and 10")
    for number in range(11):
        print(number)
    # print integers between 5 and 10
    print("\n print numbers between 5 and 10")
    for number in range(5, 11):
        print(number)
    # print even numbers between 0 and 10
    print("\n\n output even numbers between 0 and 10")
    for number in range(0, 11, 2):
        print(number)
    #print odd numbers
    print("\n\n print odd numbers")
    for value in range(1, 11, 2):
        print(value)
    #prompt user for the satr and stop values and print the numbers between start and stop
    #ge tthe start value from user and convert to integer and sdo the same for the stop value
    start_num = int(input("Select a number for a start value"))
    stop_num = int(input("Select a number for a stop value"))
    print(f"Print output numbers between {start_num} to {stop_num}")
    for number in range (start_num, stop_num + 1):
        print(number)
    # use nested for loops to print multiplicationb tables from user input
    #user will provide start and stop values for the table
    start_val = int(input("Select a number for a start value"))
    stop_val = int(input("Select a number for a stop value"))
    print(f"Print multiplication tables from {start_val} to {stop_val}")
    for table in range (start_val, stop_val + 1):
        print( f"displaying the {table} multiplication table")
        for multiple in range(1,13):
            product = table * multiple
            print(f"{table} x {multiple} = {table}")







main()