"""
Fnvtion to load menu item and price into a dictionary
input:  (string)file_path
output: (dictionary)menu
"""
def get_menu_dictionary(file_name:str) -> dict:
    data_file = open("file.txt", "r")
    #create an empty dictionary to store item: price
    menu_items = {}
    #use a loop to read the contents of a file line by line
    print("These are your options from the menu:")
    for line_of_data in data_file:
        #split the data at the comma
        item_name_and_price = line_of_data.split(",")
        #get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        #create an entry in the dictionary for the item and the price
        menu_items[item_name] = item_price
        print(f"\n{item_name}: {item_price}")
    data_file.close()
    return menu_items
def main():
    #varible is restated here
    menu_items = get_menu_dictionary("file.txt")
    get_user_input(menu_items)

def get_user_input(menu_items):
    total = 0
    while True:
        chosen_item = str(input("Item:"))
        if chosen_item.lower() == "end":
            break
        try:
            total = menu_items[chosen_item] + total
        except:
            continue
        print(f"$ {total}")




main()