def main():
    food = ["Pizza", "Burgers", "Chips"]

    print("Here are the items in the food list.")
    print(food)

    item = input("Which item should I change? \n")
    try:
        #Get the itme indez in thre list.
        item_index = food.index(item)

        #Get the value to replace it with.
        new_item = input("Enter the new value: ")

        food[item_index] = new_item

        print(food)
    
    except ValueError:
        print("That item was not found in the list.")
main()