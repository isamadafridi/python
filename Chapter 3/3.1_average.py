while True:
    m1=int(input("Enter the marks of first subject: "))
    m2=int(input("Enter the marks of second subject: "))
    m3=int(input("Enter the marks of third subject: "))

    avg=(m1+m2+m3)/3     #average of the marks
    print("The average of the marks is:", avg)


    if avg >= 90 and avg <= 100:
        print("Grade: A+")

    elif avg >= 80 and avg < 90:
        print("Grade: A")
    elif avg >= 70 and avg <80:
        print("Grade: B")
    else:
        print("Grade: C")

    cont = input("Do you want to calculate again? (yes/no): ").strip().lower()
    if cont != 'yes':
        break


