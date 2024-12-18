#ITCS102: FUNDAMENTALS OF COMPUTER PROGRAMMING

# Final Project: Python Fundamentals - Interactive Menu Program

# Objective: Develop a comprehensive text-based program in Python that serves as an interactive menu
# allowing users to navigate through multiple topics covering fundamental concepts such as print
# statements, variables, operators, conditionals, loops, lists, and functions. The program should provide a
# structured environment for learning and experimenting with Python fundamentals.

#Making it Clean to Operate
import os
os.system('cls')

#Takes Time to Determine Divisions of the Day
import datetime as dt
time = dt.datetime.now()
hour = time.strftime("%H")
user = "User"

#Greets User by the time
def greet(user):
    if 5 <= int(hour) < 12:
        print(f"Goodmorning {user}!")
    elif 12 <= int(hour) < 18:
        print(f"Goodafternoon {user}!")
    elif 18 <= int(hour) < 24:
        print(f"Goodevening {user}!")
    else:
        print(f"Staying too late ah {user}! Good Midnight {user}!")

greet(user)
user = input(f"Before We Start the Program, What is your Name {user}? ")
os.system('cls')

#Activity 1
def activity1():
    print("""
> Activity 1 was the Typing Test, But we will go the Basics of Python Programming
> Which is the "Hello World!"
> in order to print this statement, we need to use print() function
> then we use quotation to make it a string ""
> making it print("Hello World!")
""")
    
    
#Activity 2
def activity2():
    name_act2 = input("What's your name? ")
    age_act2 = input(f"Hello {name_act2}! What's your age? ")
    hobby_act2 = input(f"What is your hobby? ")
    goals_act2 = input(f"What is your goals? ")
    print(f"Hello! My name is {name_act2}, I'm {age_act2} years old. My favorite hobby is {hobby_act2}, And my goal is {goals_act2} ")    

#Main Menu
def main():
    while True:
        print("""
+----------------------------------------------------------------+      
|                           Main Menu                            |
+----------------------------------------------------------------+
| ~ Final Project of Joshua Agawin for ITCS102                   |
| ~ Choose a Lesson to View (1-7 Command)                        |
| ~ Exit Program (0)                                             |
+----------------------------------------------------------------+          
| (1) Print Statements                                           |
| (2) Variables                                                  |
| (3) Operators                                                  |
| (4) Conditionals                                               |
| (5) Loops                                                      |
| (6) Lists                                                      |
| (7) Functions                                                  |
+----------------------------------------------------------------+
| (0) Exit Program                                               |
+----------------------------------------------------------------+          
      """)
        
        choose = input(f"Hello {user}, Choose a Program to use : ").strip()
        if choose.lower() == "exit" or choose == "0":
            exit()
            break
        elif choose.lower() != "exit" or choose != "0":
            os.system('cls')
            if choose == "1":    
                while True:
                    print_statement()
                    print_choose = input("Enter a Command : ")
                    if print_choose == "0" or print_choose == "exit":
                        os.system('cls')
                        break
                    elif print_choose != "0" or print_choose != "exit":
                        os.system('cls')
                        if print_choose == "1":
                            print("activity1.py\n")
                            activity1()
                        elif print_choose == "2":
                            print("activity2.py \n")
                            activity2()
                        elif print_choose == "3":
                            print("activity4.py \n")
                        elif print_choose == "4":
                            print("code_challange1.py \n")
                        elif print_choose == "5":
                            print("code_challange2.py\n")
                        elif print_choose == "6":
                            print("code_challange4.py\n")
            elif choose == "2":
                while True:
                    variables()
                    variables_choose = input("Enter a Command : ")
                    if variables_choose == "0" or variables_choose == "exit":
                        os.system('cls')
                        break
                    elif variables_choose != "0" or variables_choose != "exit":
                        os.system('cls')
                        if variables_choose == "1":
                            print("activity3.py\n")
            elif choose == "3":
                while True:
                    operators()
                    operators_choose = input("Enter a Command : ")
                    if operators_choose == "0" or operators_choose == "exit":
                        os.system('cls')
                        break
                    elif operators_choose != "0" or operators_choose == "exit":
                        os.system('cls')
                        if operators_choose == "1":
                            while True:
                                arithmetic_operators()
                                arithmetic_operators_choose = input("Enter a Command : ")
                                if arithmetic_operators_choose == "0" or arithmetic_operators_choose == "exit":
                                    os.system('cls')
                                    break
                                elif arithmetic_operators_choose != "0" or arithmetic_operators_choose != "exit":
                                    os.system('cls')
                                    if arithmetic_operators_choose == "1":
                                        print("activity4.py \n")
                                    elif arithmetic_operators_choose == "2":
                                        print("activity5.py \n")
                                    elif arithmetic_operators_choose == "3":
                                        print("code_challange3.py \n")
                                    elif arithmetic_operators_choose == "4":
                                        print("code_challange4.py\n")
                                    elif arithmetic_operators_choose == "5":
                                        print("code_challange5.py \n")
                                    elif arithmetic_operators_choose == "6":
                                        print("code_challange7.py \n")
                        elif operators_choose == "2":
                            while True:
                                assignment_operators()
                                assignment_operators_choose = input("Enter a Command : ")
                                if assignment_operators_choose == "0" or assignment_operators_choose == "exit":
                                    os.system('cls')
                                    break
                                elif assignment_operators_choose != "0" or assignment_operators_choose != "exit":
                                    os.system('cls')
                                    if assignment_operators_choose == "1" :
                                        print("activity6.py \n")
                                    elif assignment_operators_choose == "2":
                                        print("code_challange7.py\n")
                        elif operators_choose == "3":
                            while True:
                                comparison_operators()
                                comparison_operators_choose = input("Enter a Command : ")
                                if comparison_operators_choose == "0" or comparison_operators_choose == "exit":
                                    os.system('cls')
                                    break
                                elif comparison_operators_choose != "0" or comparison_operators_choose != "exit":
                                    os.system('cls')
                                    if comparison_operators_choose == "1":
                                        print("activity7.py \n")
                                    elif comparison_operators_choose == "2":
                                        print("activity9.py \n")
                                    elif comparison_operators_choose == "3":
                                        print("code_challange6.py\n")
                                    elif comparison_operators_choose == "4":
                                        print("code_challange7.py")
                        elif operators_choose == "4":
                            while True:
                                logical_operators()
                                logical_operators_choose = input("Enter a Command : ")
                                if logical_operators_choose == "0" or logical_operators_choose == "exit":
                                    os.system('cls')
                                    break
                                elif logical_operators_choose != "0" or logical_operators_choose != "exit":
                                    os.system('cls')
                                    if logical_operators_choose == "1":
                                        print("activity9.py \n")
                                    elif logical_operators_choose == "2":
                                        print("activity10.py \n")
            
            elif choose == "4":
                while True :
                    conditionals()
                    conditionals_choose = input("Choose a Command : ")
                    if conditionals_choose == "0" or conditionals_choose == "exit":
                        os.system('cls')
                        break
                    elif conditionals_choose != "0" or conditionals_choose != "exit":
                        os.system('cls')
                        if conditionals_choose == "1":
                            print("activity7.py\n")
                        elif conditionals_choose == "2":
                            print("activity9.py\n")
                        elif conditionals_choose == "3":
                            print("activity10.py")
                        elif conditionals_choose == "4":
                            print("code_challange6.py\n")
                        elif conditionals_choose == "5":
                            print("code_challange7.py \n")
                
            elif choose == "5":
                while True:
                    loop()
                    loop_choice = input("Choose a Command : ")
                    if loop_choice == "0" or loop_choice == "exit":
                        os.system('cls')
                        break
                    elif loop_choice != "0" or loop_choice != "exit":
                        os.system('cls')
                        if loop_choice == "1":
                            while True:
                                for_loop()
                                for_loop_choice = input("Choose a Command : ")
                                if for_loop_choice == "0" or for_loop_choice == "exit":
                                    os.system('cls')
                                    break
                                elif for_loop_choice != "0" or for_loop_choice != "exit":
                                    os.system('cls')
                                    if for_loop_choice == "1":
                                        print("activity11.py\n")
                                    elif for_loop_choice == "2":
                                        print("activity12.py \n")
                                    elif for_loop_choice == "3":
                                        print("activity13.py \n")
                                    elif for_loop_choice == "4":
                                        print("activity14.py \n")
                                    elif for_loop_choice == "5":
                                        print("activity15.py \n")
                                    elif for_loop_choice == "6":
                                        print("activity16.py \n")
                                    elif for_loop_choice == "7":
                                        print ("activity17.py \n")
                                    elif for_loop_choice == "8":
                                        print("activity18.py \n")
                                    elif for_loop_choice == "9":
                                        print("code_challange8.py \n")
                                    elif for_loop_choice == "10":
                                        print("code_challange9.py \n")
                                    elif for_loop_choice == "11":
                                        print("code_challange10.py\n")
                                    elif for_loop_choice == "12":
                                        print("code_challange11.py \n")
                                    elif for_loop_choice == "13":
                                        print("code_challange12.py \n")
                                    elif for_loop_choice == "14":
                                        print("code_challange13.py")
                        elif loop_choice == "2":
                            while True:
                                while_loop()
                                while_loop_choice = input("Choose a Command : ")
                                if while_loop_choice == "0" or while_loop_choice == "exit":
                                    os.system('cls')
                                    break
                                elif while_loop_choice != "0" or while_loop_choice != "exit":
                                    os.system('cls')
                                    if while_loop_choice == "1":
                                        print("activity19.py \n")
                                    elif while_loop_choice == "2":
                                        print("code_challange14.py \n")
                        elif loop_choice == "3":
                            while True:
                                hybrid_loop()
                                hybrid_loop_choice = input("Choose a Command : ")
                                if hybrid_loop_choice == "0" or hybrid_loop_choice == "exit":
                                    os.system('cls')
                                    break
                                elif hybrid_loop_choice != "0" or hybrid_loop_choice == "exit":
                                    os.system('cls')
                                    if hybrid_loop_choice == "1":
                                        print("activity20.py\n")
            elif choose == "6":
                while True:
                    list()
                    list_choice = input("Choose a Command : ")    
                    if list_choice == "0" or list_choice == "exit":
                        os.system('cls')
                        break
                    elif list_choice != "0" or list_choice != "exit":
                        os.system('cls')
                        if list_choice == "1":
                            print("activity25.py \n")
            elif choose == "7":
                while True:
                    function()
                    function_choice = input("Choose a Command : ")
                    if function_choice == "0" or function_choice == "exit":
                        os.system("cls")
                        break
                    elif function_choice != "0" or function_choice != "exit":
                        os.system('cls')
                        if function_choice == "1":
                            print("activity8.py \n")
                        elif function_choice == "2":
                            print("activity21.py \n")
                        elif function_choice == "3":
                            print("code_challange16.py \n")

                
                        
                    

#Print Statements Menu
def print_statement():
    print("""
+----------------------------------------------------------------+      
|                    [1] Print Statements                        |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity1.py            | (4) code_challange1.py           |
| (2) activity2.py            | (5) code_challange2.py           |
| (3) activity4.py            | (6) code_challange4.py           |
+-----------------------------+----------------------------------+
| (0) Go Back to Main Menu                                       |           
+-----------------------------+----------------------------------+          
      """)
    
#Variables Menu
def variables():
    print("""
+----------------------------------------------------------------+      
|                        [2] Variables                           |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity3.py            |                                  |
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+-----------------------------+----------------------------------+          
      """)   
    
#Operators Menu
def operators():
    print("""
+----------------------------------------------------------------+      
|                        [3] Operators                           |
+----------------------------------------------------------------+          
| (1) Arithmetic Operators                                       |                                       
| (2) Assignment Operators                                       |
| (3) Comparison Operators                                       |
| (4) Logical Operators                                          |                 
+----------------------------------------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+----------------------------------------------------------------+          
      """)
    
#Arithmetic Operators Menu
def arithmetic_operators():
    print("""
+----------------------------------------------------------------+      
|                [3.1] Arithmetic Operators                      |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity4.py            | (3) code_challange3.py           | 
| (2) activity5.py            | (4) code_challange4.py           |
|                             | (5) code_challange5.py           |                                           
|                             | (6) code_challange7.py           |                                         
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Operator Menu                                   |
+-----------------------------+----------------------------------+          
      """)           

#Assignment Operators Menu
def assignment_operators():
    print("""
+----------------------------------------------------------------+      
|                [3.2] Assignment Operators                      |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity6.py            | (2) code_challange7.py           | 
|                             |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Operator Menu                                   |
+-----------------------------+----------------------------------+          
      """)  
    
#Comparison Operators Menu
def comparison_operators():
    print("""
+----------------------------------------------------------------+      
|                [3.3] Comparison Operators                      |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity7.py            | (3) code_challange6.py           | 
| (2) activity9.py            | (4) code_challange7.py           |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Operator Menu                                   |
+-----------------------------+----------------------------------+          
      """)   
    
#Logical Operators Menu
def logical_operators():
     print("""
+----------------------------------------------------------------+      
|                [3.4] Logical Operators                         |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity9.py            |                                  | 
| (2) activity10.py           |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Operator Menu                                   |
+-----------------------------+----------------------------------+          
      """)

#Conditionals Menu
def conditionals():
    print("""
+----------------------------------------------------------------+      
|                       [4] Conditionals                         |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity7.py            | (4) code_challange6.py           | 
| (2) activity9.py            | (5) code_challange7.py           |
| (3) activity10.py           |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+-----------------------------+----------------------------------+          
      """)

#loop menu
def loop():
    print("""
+----------------------------------------------------------------+      
|                        [5] Loops                               |
+----------------------------------------------------------------+          
| (1) for loop                                                   |                                       
| (2) while loop                                                 |
| (3) hybrid loop                                                |                 
+----------------------------------------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+----------------------------------------------------------------+          
      """)


#for loop Menu
def for_loop():
    print("""
+----------------------------------------------------------------+      
|                      [5.1] for loop                            |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity11.py           | (9) code_challange8.py           | 
| (2) activity12.py           | (10) code_challange9.py          |
| (3) activity13.py           | (11) code_challange10.py         |                                        
| (4) activity14.py           | (12) code_challange11.py         |                                        
| (5) activity15.py           | (13) code_challange12.py         |                                        
| (6) activity16.py           | (14) code_challange13.py         |                                        
| (7) activity17.py           |                                  |                                        
| (8) activity18.py           |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Loops Menu                                      |
+-----------------------------+----------------------------------+          
      """)    
      
#while loop menu
def while_loop():
    print("""
+----------------------------------------------------------------+      
|                      [5.2] while loop                          |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity19.py           | (2) code_challange14.py          |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Loops Menu                                      |
+-----------------------------+----------------------------------+          
      """)

#hybrid loop menu
def hybrid_loop():
    print("""
+----------------------------------------------------------------+      
|                      [5.3] hybrid loop                         |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity20.py           |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Loops Menu                                      |
+-----------------------------+----------------------------------+          
      """)

#list menu
def list():
    print("""
+----------------------------------------------------------------+      
|                      [6] Lists                                 |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity25.py           |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+-----------------------------+----------------------------------+          
      """)

#function menu
def function():
    print("""
+----------------------------------------------------------------+      
|                      [7] Functions                             |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity8.py            | (3) code_challange16.py          |                                        
| (2) activity21.py           |                                  |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+-----------------------------+----------------------------------+          
      """)            

def exit():
    os.system('cls')
    print(f"Thank you for using the Program! Have a Great Day {user}!")

main()
