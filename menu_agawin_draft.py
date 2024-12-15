import os
os.system('cls')

import datetime as dt
time = dt.datetime.now()
hour = time.strftime("%H")
user = "User"
def greet(user):
    if 5 <= int(hour) < 12:
        print(f"Goodmorning {user}")
    elif 12 <= int(hour) < 18:
        print(f"Goodafternoon {user}")
    elif 18 <= int(hour) < 24:
        print(f"Goodevening {user}")
    else:
        print(f"Good Midnight! {user}")

greet(user)
user = input(f"Before We Start the Program, What is your Name {user}? ")

greet(user)

choose_menu = input("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Code Compilation 2024 for ITCS102
                    
code_challange1.py = 1               activity1.py = 101         activity14.py = 114
code_challange2.py = 2               activity2.py = 102         activity15.py = 115
code_challange3.py = 3               activity3.py = 103         activity16.py = 116
code_challange4.py = 4               activity4.py = 104         activity17.py = 
code_challange5.py = 5               activity5.py = 105                         
code_challange6.py = 6               activity6.py = 106
code_challange7.py = 7               activity7.py = 107
code_challange8.py = 8               activity8.py = 108                                             
code_challange9.py = 9               activity9.py = 109
code_challange10.py = 10             activity10.py = 110
code_challange11.py = 11             activity11.py = 111
code_challange12.py = 12             activity12.py = 112
code_challange13.py = 13             activity13.py = 113
code_challange14.py = 14
code_challange15.py = 15
code_challange16.py = 16            
                            
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++                      
                    """)
