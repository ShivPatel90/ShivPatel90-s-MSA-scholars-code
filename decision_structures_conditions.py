# the file demos decision structures and conditions
def main():
    a = 7
    b = 4
    #exploring conditions
    print(f"A is greater than B: {a > b}")
    print(f"B is greater than A: {a > b}")
    print(f"A is equal to B: {a == b}")
    #comparison operators:
    #less than: <, greater than: >, less than or equal to: <=, greater than or equal to >=
    #equal to : ==
    #create a decision structgure to determine if a and b are equal
    if a > b: 
        print(f"{a} is greater and {b} ")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b} ")
    #create a deicsion structure to print a letter grade based on a test score
    # A: 100-90 B:89-80 c: 79-70 D:69-60 F: less than 60 
    print("grade decision: 1")
    test_score = int(input("what was your test score number"))
    if ((test_score<= 100) and (test_score >= 90 )):
        print(f"{test_score}---> A")
    elif ((test_score<= 89) and (test_score >= 80 )):
        print(f"{test_score}---> B")
    elif ((test_score<= 79) and (test_score >= 70 )):
        print(f"{test_score}---> C")
    elif ((test_score<= 69) and (test_score >= 60 )):
        print(f"{test_score}---> D")
    else:
        print(f"{test_score}---> F")

main()