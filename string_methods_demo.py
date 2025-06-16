def main():
    my_name = "shiv"
    #capitalize a string
    print(my_name.capitalize())
    #make a string uppercase
    print(my_name.upper())
    #make a last name lowercase
    last_name = "PATEL"
    print(f" my name is {my_name} {last_name.lower()} ")
    #determine if a sring starts with a set of characters
    print(":\Loop through a string USing startswith() method")
    print(my_name.startswith("s") or my_name.startswith("S"))

    if(not my_name.startswith("sh") and not my_name.startswith("Sh")):
        print(f"you spelled {my_name} incorrectly")
    else:
        print(f" You spelled {my_name} correctly")
    print(f"\nUsing endswith() method")
    print(f" {my_name} ends with {my_name.endswith("v")}")
    print("\Loop through a string using the find() method")
    print(my_name.find("v", 0, 4))
    search_letter = "iv" 
    if(my_name.find(search_letter) == -1):
        print(f"there is no {search_letter} in {my_name}")
    else:
        print(my_name.find(search_letter))
    #loop through a string
    print("\Loop through a string")
    for letter in my_name:
        print(letter)
    print(f"{my_name} has {len(my_name)}")
    #pirnt the letters in a string withg index position
    for letter_index in range(len(my_name)):
        print(f"letter {letter_index}: {my_name[letter_index]}")
    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    search_word = "dog"
    start_index = 0
    dog_index = 0 
    number_of_dogs = 0
    # write a cpde that counts the number of the word dog.
    # int the sentence excpected output : 3
    # use a while loop 
    while True:
        #search for the first occurence of the word(dog)
        #if we find a dog add 1 to some variable of dogs we found
        #continue searchin the string from the next index after the dog we found
        #do this until we dont find any mroe dogs


        dog_index = sentence.find(search_word, start_index)
        if start_index == -1:
            break
        else:
            number_of_dogs += 1 
            start_index = dog_index + 1
    print(f"there are {number_of_dogs} {search_word} in the sentence")

    print("\n Usingf the split() method")
    car_info = "Ferrarai, f-50, 2021, 500000, 4.8"
    car_data = car_info.split(",")
    print(car_data[0])



main()