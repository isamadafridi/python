'''6. Calories from Fat and Carbohydrates
A nutritionist who works for a fitness club helps members by evaluating their diets. As part
of her evaluation, she asks members for the number of fat grams and carbohydrate grams
that they consumed in a day. Then, she calculates the number of calories that result from
the fat, using the following formula:
    calories from fat = fat grams * 9
Next, she calculates the number of calories that result from the carbohydrates, using the
following formula:
    calories from carbs = carb grams * 4
The nutritionist asks you to write a program that will make these calculations.
    '''

def calories_from_fat(fat_grams):
    return fat_grams * 9

def calories_from_carbs(carb_grams):
    return carb_grams * 4

def main():
    fat_grams = float(input("Enter the number of fat grams consumed: "))
    carb_grams = float(input("Enter the number of carbohydrate grams consumed: "))

    fat_calories = calories_from_fat(fat_grams)
    carb_calories = calories_from_carbs(carb_grams)

    print(f"The number of calories from fat is: {fat_calories:.2f}")
    print(f"The number of calories from carbohydrates is: {carb_calories:.2f}")

main()