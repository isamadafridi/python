import pet_class

def main():
    name  = input('Enter the pet\'s name: ')
    animal_type = input('Enter the type of animal: ')
    age = int(input('Enter the pet\'s age: '))
    breed = input('Enter the breed of the dog: ')

    pet = pet_class.Pet(name, animal_type, age)
    dog = pet_class.Dog(breed)

    print('Here is the data you provided:')
    print('Pet name:', pet.get_name()) 
    print('Animal type:', pet.get_animal_type())
    print('Age:', pet.get_age())
    print('Breed:', dog.get_breed())

main()