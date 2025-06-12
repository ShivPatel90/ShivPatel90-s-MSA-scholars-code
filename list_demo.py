#this file will demo lists in python 
def main():
    #we dont want to have to do this:
    #name1 = "john"
    #name2 = "alice"
    #  use a list instead
    name_list = ["john", "mary", "alice", "bob"]
    list_of_integers = [10, 9, 7, 100]
    random_datatype_list = ["syd", 10, 22 ,2, "frank"]
    print(name_list)

    #add an item 
    name_list.append("jane")
    list_of_integers.append(32)
    print(name_list)
    print(list_of_integers)
    # get the number of items in a list'
    print(f"\n number of items in the names list")
    number_of_items = len(name_list)
    print(f" print number of item in names list: {number_of_items}")
    #get the values from our list
    # get the first valye from our list of integers
    print(f"\n first item in integer list:{list_of_integers[0]}")

    print(f"print foruth item of the integer list{list_of_integers[3]}")
    #print all the item from the list of inter=gers
    print("\n integer list list items")
    for item in list_of_integers:
        print(item)

    print("\n integer list items using the item indexes")
    # get number of items in integer list
    number_of_integers = len(list_of_integers)

    for index in range(number_of_integers):
        print(f"item {index}: {list_of_integers[index]}")

main()