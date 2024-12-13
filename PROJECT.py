#Makes it Cleaner to Re-Run Program
import os
os.system('cls')

#Date import
import datetime
current_date = datetime.datetime.now()
current_hour = int(current_date.strftime("%H")) 

#Activity 1 
print("Hello World!")

#Activity 2
name = input("Hello User!, What is your Name ? ")
if current_hour > 12:
    print("Yes it is greater than 12")