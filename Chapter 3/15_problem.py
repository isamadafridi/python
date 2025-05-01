'''15. Time Calculator
Write a program that asks the user to enter a number of seconds and works as follows:
• There are 60 seconds in a minute. If the number of seconds entered by the user is greater
than or equal to 60, the program should convert the number of seconds to minutes and
seconds.
• There are 3,600 seconds in an hour. If the number of seconds entered by the user is
greater than or equal to 3,600, the program should convert the number of seconds to
hours, minutes, and seconds.
• There are 86,400 seconds in a day. If the number of seconds entered by the user is
greater than or equal to 86,400, the program should convert the number of seconds to
days, hours, minutes, and seconds.
************************************************************
Ask from user to enter a number of seconds
Check if the number of seconds is greater than or equal to 60
If yes, convert the number of seconds to minutes and seconds
Check if the number of seconds is greater than or equal to 3600
If yes, convert the number of seconds to hours, minutes and seconds
Check if the number of seconds is greater than or equal to 86400
If yes, convert the number of seconds to days, hours, minutes and seconds


'''
while True:
    sec = int(input("Enter a number of seconds: "))
   
    if sec >= 3600:
        hour = sec // 3600
        min = sec % 3600 // 60
        sec = sec % 60
        print("Hours: ", hour, "Minutes: ", min, "Seconds: ", sec)
    elif sec >= 60:
        min = sec  // 60
        sec = sec % 60
        print("Minutes: ", min, "Seconds: ", sec)




















    input("Press Enter to continue...")

