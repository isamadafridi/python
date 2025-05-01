import cell_phone_c

def main():
    manu = input('Enter the manufacturer: ')
    model = input('Enter the model number: ')
    price = float(input('Enter the retail price: '))

    phone = cell_phone_c.CellPhone(manu, model, price)

    #Display the data that was entered
    print('Here is the data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model Number:', phone.get_model())   
    print('Retail Price:', phone.get_retail_price())

main()