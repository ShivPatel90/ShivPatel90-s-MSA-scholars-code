# set up prompts and variables
# it is saying that if you enter the input both correctly then the loop will break but if there is an exception then it will print error and make you retry

def  calculate_wage(work_hours, hourly_wage):
    wages_pre_taxes =  work_hours * hourly_wage * 350
    tax_amount = wages_pre_taxes * .12 
    wages_post_tax = wages_pre_taxes - tax_amount
    return wages_pre_taxes, wages_post_tax, tax_amount

def report(wages_pre_taxes, tax_amount, wages_post_tax):
    print(f"\n wages pretax:{wages_pre_taxes}\n tax amount:{tax_amount} \n wages post taxes: {wages_post_tax}")


def main():
    while True:
        try:
            work_hours = float(input("Enter number of hours you have worked"))
            if work_hours <= 24 and work_hours >= 0:
                break
            else:
                continue
        except:
            print("ERROR: ENTER NUMBER FROM 0-24")


    while True:
        try:
            hourly_wage = float(input("What is your hourly wage"))
            break
        except:
            print("ERROR: ENTER A NUMBER")

    wages_pre_taxes, wages_post_tax, tax_amount = calculate_wage(work_hours, hourly_wage)
    report(wages_pre_taxes, tax_amount, wages_post_tax)

main()