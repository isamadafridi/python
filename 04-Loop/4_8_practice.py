# Get the number of students and test scores per student
num_students = int(input('How many students do you have? '))
num_test_scores = int(input('How many test scores per student? '))

# Loop through each student
for student in range(num_students):
    total = 0.0  # Initialize total score for each student
    print('\nStudent number', student + 1)
    print('–––––––––––––––––')
    
    # Loop through each test score
    for test_num in range(num_test_scores):
        score = float(input(f'Test number {test_num + 1}: '))
        total += score  # Add score to total

    # Calculate and display average
    average = total / num_test_scores
    print(f'The average for student number {student + 1} is: {average:.2f}')
