import cell_phone_c

def main():
    phone = make_list()
    print('Here is the data that you entered:')
    display_list(phone)

def make_list():
    # Create an empty list
    phone_list = []

    # Add five CellPhone objects to the list.
    print('Enter data for five phones.')
    for count in range(1, 6):
        print('Phone number ' + str(count) + ':')
        manu = input('Enter the manufacturer: ')
        model = input('Enter the model number: ')
        price = float(input('Enter the retail price: '))
        print()

        # Create a new CellPhone object in memory and assign it to the phone variable.
        phone = cell_phone_c.CellPhone(manu, model, price)

        phone_list.append(phone)
        return phone_list

def display_list(phone_list):
    for item in phone_list:
        print(item.get_manufact())
        print(item.get_model())
        print(item.get_retail_price())
        print()

main()