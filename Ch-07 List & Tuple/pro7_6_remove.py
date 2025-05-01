def main():
    food = ['rice', 'beans', 'bread', 'pasta', 'cereal', 'potatoes']
    print("The list before removing")
    print(food)

    item = input("Enter the item to remove: ")
    try:
        food.remove(item)
        print(f"Item {item} removed")
        print("The list after removing")
        print(food)

    except ValueError:
        print(f"Item {item} not found")
        print("The list after removing")
        print(food)
main()