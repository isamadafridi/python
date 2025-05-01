import vehicle

def main():
    make = input('Enter the car\'s make: ')
    model = input('Enter the car\'s model: ')
    mileage = float(input('Enter the car\'s mileage: '))
    price = float(input('Enter the car\'s price: '))
    doors = int(input('Enter the number of doors: '))

    used_car = vehicle.Car(make, model, mileage, price, doors)

    # Display the car's data.
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Mileage:', used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Number of doors:', used_car.get_doors())

main()