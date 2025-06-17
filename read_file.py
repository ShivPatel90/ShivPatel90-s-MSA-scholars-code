def main():
    #open file.txt
    data_file = open("file.txt", "r")
    #create an empty dictionary to store item: price
    menu_items = {}
    #use a loop to read the contents of a file line by line
    for line_of_data in data_file:
        #split the data at the comma
        item_name_and_price = line_of_data.split(",")
        #get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])
        #create an entry in the dictionary for the item and the price
        menu_items[item_name] = item_price
main()