def main():
    # fruit = ["apple", "banana", "mango"]

    # search = input("Enter a friut name you eant to search: ")

    # if search  in fruit:
    #     print(f"{search} fruit found")

    # else:
    #     print(f"{search} friut not found")
    names = ['Jim', 'Jill', 'John', 'Jasmine']
    search = input("Enter a name you want to search: ")
    # if search not in names:
    #     print(f'Cannot find {search}.')
    # else:
    #     print("Jasmine's family:")
    #     print(names)

    if search  in names:
        print("Jasmine's family:")
        print(names) # print all the names in the list
    else:
        print(f'Cannot find {search}.')
    


main()
