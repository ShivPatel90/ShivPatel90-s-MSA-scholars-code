print("hello world")
# create var to store name
first_name =  "Shiv"
# print first name
print(first_name)
# use a statement to tell name
print("My name is", first_name)
# create a variable to stroe last name
last_name = "Patel"
# write full name
print(" My full name is", first_name, last_name, sep = "---")
# create variables to store age height and weight and assign them values
age = 16
height = 72
weight = 200
# print a sentence with age weight and height
print(F"My name is {first_name} {last_name}\nI am {age} years old and I am {height} and {weight}")
# get and print data type for age weight and height
print(type(age))
print(type(weight))
print(type(height))
# write 3 print statements using string interpolation (fstring) to print desccriptive sentences for data types
print(f" The variable given for age {type(age)},. The variable given for weight, {type(weight)}.The variable given for height, {type(height)}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f" the sum of {number_1} and {number_2} is equal to {total}")