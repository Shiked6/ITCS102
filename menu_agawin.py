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

#Activity 3
def activity3():
    print("\nBiographical Data / Bio Data")
    name_act3 = input('\nFull Name : ')
    gender_act3 = input('Gender : ')
    address_act3 = input("Home Address: ")
    age_act3 = input("Age : ")
    bday_act3 = input("Birth Day : ")
    bmonth_act3 = input('Birth Month : ')
    byear_act3 = input('Birth Year : ')
    bplace_act3 = input('Place of Birth: ')
    fname_act3 = input("Father's Name : ")
    mname_act3 = input("Mother's Name : ")
    phone_act3 = input('Contact Number : ')
    email_act3 = input("Email Address: ")

    print("Good Day!, I am", name_act3, "I am from", address_act3, "and I am",age_act3,"years old","I am a", gender_act3, "Born on",bmonth_act3, bday_act3, byear_act3, "In the place of",bplace_act3,".")
    print("My Father's Name is ", fname_act3, "And my Mother's Name is", mname_act3, "You can contact me by",phone_act3,"And my Email is",email_act3,".","Thank you and Have a Wonderful Day!.")

    print("\nCreated By : Joshua Ezekiel A. Agawin\nCourse & Section : BSIT_1C\nDate Created : 09/04/2024_Wednesday\nDate Submitted : 09/05/2024_Thursday\nThank you!")

#Activity 4
def activity4():
    num1_act4 = eval(input("Enter a number ---> "))
    num2_act4 = eval(input("Enter another number ---> "))
    sum_act4 = num1_act4 + num2_act4
    print("The sum of" , num1_act4,"and", num2_act4,"is", sum_act4)
    print("""
Created By : Joshua Ezekiel A. Agawin
Course & Section : BSIT_1C
Date Created : 09/06/2024_Friday
""")
    
#Activity 5
def activity5():
    print("Fahrenheit to Celsius Converter Program\n\nFormula used : C = (F - 35) * 5 / 9")
    temp_act5 = eval(input("\nEnter temperature in Fahrenheit : "))
    cel_act5 = temp_act5 - 32
    cel2_act5 = cel_act5 * 5
    cel3_act5 = cel2_act5 / 9
    cel4_act5 = round(cel3_act5, 2) 
    print("The Conversion of",temp_act5 ," degrees Fahrenheit is ",cel4_act5 , "degrees Celsius.")
    print("\nCreated By : Joshua Ezekiel A. Agawin\nCourse and Section : BSIT_1C\nDate Created : 09/11/2024 (Wednesday)\n Thank you!")

#Activity 6
def activity6():
  x_act6 = 5
  print(f"Assigning value [x = {x_act6}]")
  #Updating the Value of x
  x_act6 = x_act6 + 10
  print(f"Updating the Value of X [x = x + 10] = {x_act6}")
  x_act6 = x_act6 + 15
  print(f"Updating the Value of X [x = x + 15] = {x_act6}")
  #simplified version
  x_act6 += 20
  print(f"Simplified Version [x += 20] = {x_act6}")
  #other arithmetic
  x_act6 -= 25
  print(f"Other Arithmetic [x -= 25] = {x_act6}")
  
  print("\nBy Joshua Ezekiel A. Agawin,\nFrom BSIT_1C\nDate Created : 09/16/2024\nThank you!")

#Activity 7
def activity7():
  miner_act7 = input("Please put your name --> ")
  gold_act7 = 0
  miner_action_act7 = input("Did you mine any gold today? Yes or No? ")
    
  if miner_action_act7.lower() == "yes" :
    gold_act7 += 1
    print(f"Hi {miner_act7}, Today you have a total of {gold_act7} gold")
  elif miner_action_act7.lower() == "no" :
    print(f"Hi {miner_act7}, Today you have a total of {gold_act7} gold")
  else :
    print("You have type a different word that is not yes or no.. Try Again..")
    
  print("\nBy Joshua Ezekiel A. Agawin,\nFrom BSIT_1C\nDate Created : 09/16/2024\nThank you!")

#Activity 8 
#Storing Variables
user_data = {}
accounts = {}

#Create Account
def create_user():
    print("activity8.py \n")
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists. Please choose another.")
        return
    password = input("Enter a password: ")
    user_data[username] = password
    print("User created successfully!")

#Login Account
def login():
    print("activity8.py \n")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if user_data.get(username) == password:
        print()
        print(f"Login successful! Welcome,   {username}  !")
    else:
        print("Invalid username or password.")

#Activity 8 Menu
def activity8_menu():
    print("""
+----------------------------------------------------------------+      
|                           Activity 8                           |
+----------------------------------------------------------------+
| > Register and Login System                                    |
| > Use the 2 Commands to Operate                                |
+----------------------------------------------------------------+          
| (1) Register Account                                           |
| (2) Login Account                                              |
+----------------------------------------------------------------+
| (0) Back to Functions Menu                                     |
+----------------------------------------------------------------+          
      """)

#Activity 9
def activity9():
  a_act9 = eval(input("Age Bracket Determiner \nEnter Age : "))
  
  if 1 <= a_act9 <= 7 :
    print("Toddler")
  elif 8 <= a_act9 <= 13 :
    print("Pre Teen")
  elif 14 <= a_act9 <= 18 :
    print("Teenager")
  elif 19 <= a_act9 <= 31 :
    print("Early Adulthood")
  elif 32 <= a_act9 <= 45 :
    print("Mid Adulthood")
  elif 46 <= a_act9 <= 59 :
    print("Post Adulthood")
  elif 60 <= a_act9 <= 150:
    print("Senior")
  else :
    print("Invalid Age")
  
  print("\nMade By : Joshua Ezekiel A. Agawin \nFrom : BSIT-1C\nDate Created : 09/20/2024\n Thank You!")

#Activity 10
def activity10():
    name_act10 = input("Enter Your Name: ")

    isStudent_act10 = input("Are you a student of DLL(Yes/No): ")

    if isStudent_act10.lower()=="yes":
        print("Welcome to the DLL BSIT Scholarship form") 
        Avida_act10 = input("Are you from Avida? (yes/no):")
        if Avida_act10.lower()=="yes":
            print("Please fillup the second form")
            yearlevel_act10 = input("What year are you currently enrolled?\nF-Freshnen\nS-Sophomore\nJ-Junior\nR-Senior\nPlease input your answer here: ")

            if yearlevel_act10.lower() == 'f':
                print(f"Hi {name_act10}, Freshmen, Welcome to DLL")

            elif yearlevel_act10.lower() == 's': 
                print(f"Hi {name_act10}, Sophomore, Welcome to DLL")

            elif yearlevel_act10.lower() == 'j': 
                print(f"Hi {name_act10}, Junior, Welcome to DLL")

            elif yearlevel_act10.lower() == 'r': 
                print(f"Hi {name_act10}, Senior, Welcome to DLL")

            else:
                print("Invalid Option")
            IsNeeded_act10 = input("Would you like to apply for a scholarship? (yes/no): ")

            if IsNeeded_act10.lower() == "yes":
                print("Scholarship approved")
            else:
                print("Unfortunately, this scholarship grant are only for residents of Silangan Mayao only")
            print("Your form has been successfully submitted")
            print()
    

#Activity 11
def activity11():
    for x in range(1,5):
        print("input loop")
        name_act11 = input("Hi! Please input your name: ")
        print(f"Hi {name_act11}")

#Activity 12
def activity12():
  #Try the following values :
  #Starting Point is 10
  #Stopping Point is 1
  #What would be the output of the following value?

  for cycle in range(10,0,-1):
      print(cycle)

#Activity 13
def activity13():
  #Factorial = 1
  #Enter any Number : 
  
  print(f"Factorial Calculator\n")
  
  factorial_act13 = eval(input("Enter any number to Factor : "))
  result_act13 = 1
  for x_act13 in range(factorial_act13,0,-1):
      result_act13 *= x_act13
      
  print(f"The Factorial of {factorial_act13} is {result_act13}")
  print(f"""
  Created By : Joshua Ezekiel A. Agawin
  From BSIT-1C
  Date Created : 10/16/2024
  Thank you!""")

#Activity 14
def activity14():
    for x_act14 in range(0,11):
        print(x_act14, end=" ")
        for y_act14 in range(0,11):
            print(" ❤️ ",end="")
        print()
  
    print("For Sir Mesiera")
  
    print(f"""Made by Joshua Ezekiel A. Agawin
  From BSIT-1C
  Made on 10-21-2024 (Monday)
  Thank you!
  """)
    
#Activity 15
def activity15(): 
    for x_act15 in range(1,11,1):
        print(end="")

        for y_act15 in range(x_act15,11,1):
            print(end=" ")
        print("* " * x_act15)

        for b_act15 in range(11,x_act15,-1):
            print(end=" ")
        print("* " * x_act15)

#Activity 16
def activity16():
    t_act16 = int(input("Enter a number range: "))
    for x_act16 in range(1,t_act16):

        for a_act16 in range(1,x_act16,1):
            print(" ",end="  ")

        for b_act16 in range(t_act16,x_act16,-1):
            print("* ",end=" ")

#Activity 17
def activity17():
  col_act17 = eval(input("Enter number of column : "))
  
  for x_act17 in range(1,11):
      for y_act17 in range(1,col_act17+1):
          print(f"{x_act17*y_act17}",end="\t")
      print()

#Activity 18
def activity18():
  tri_act18 = eval(input("Enter number of triangles : "))
  
  for x_act18 in range(1,5):
      for  r_act18 in range(1,tri_act18+1):
          for y_act18 in range(1,x_act18+1):
              print("*",end=" ")
          
          for z_act18 in range(5,x_act18,-1):
              print(" ",end=" ")
      print()

#Activity 19
def activity19():
    tama_act19 = True

    while tama_act19 == True:
        ask_act19 = input("Enter your name: ")
        if ask_act19.lower() == "stop":
            break
            ask_act19 == False

#Activity 20
def activity20():
    import os
    tama_act20 = True
    no_act20 = 0
    while tama_act20 == True:
        ask_act20 = input("Would you like to continue? (yes/no): ")
        if ask_act20.lower() == "no":
            print("Program Terminated")
            break
            ask_act20 == False
        else:
            os.system('cls')
            for x_act20 in range(1,6):
                no_act20 += 1
                for r_act20 in range (1,no_act20+1):
                    for y_act20 in range(1,x_act20+1):
                        print("*",end=" ")
                    for z_act20 in range(5,x_act20,-1):
                        print(" ",end= " ")
                print()
            continue    

#Activity 21
def activity21():
    print("""
> Activity 21 is the compilation of all codes using functions
> def activity1-25():
> calling the function by activity1-25()
> def code_challange1-16():
> calling the function by code_challange1-16()
          """)

#Activity 22
def activity22():
    pass

#Activity 23
def activity23(number_act23):  # Module to calculate factorial
    """This function computes the factorial of any number given."""
    fact_act23 = 1
    for x_act23 in range(number_act23, 0, -1):  # Loop from the number down to 1
        fact_act23 *= x_act23
    return fact_act23  # Return the factorial result

# Call the function and print the result

#Activity 24
def activity24():
    while True:
        print("""
    +-----------------------+
    | past, present, future |
    +-----------------------+
    """)
        x_act24 = {"past":"Yesterday","present":"Today","future":"Tommorow"}
        y_act24 = input("Choose one from the box : ").strip()
        if y_act24 in x_act24:
            print(x_act24[y_act24])
            break
        else:
            os.system('cls')
            print("Wrong Input, Try Again...")
            continue

#Activity 25
def activity25():
    courses_act25 = ["BSIT", "BSA", "BSAIS", "BTVTED", "BSSW", "BSPA", "Delete w/o index", "Delete with index"]
    courses_act25.remove("Delete w/o index")
    courses_act25.pop()
    courses_act25.append("DHRS")
    courses_act25.insert(0, "ABELS")
    print(courses_act25)

#Code Challange 1
def code_challange1():
  print ("By : Joshua Ezekiel A. Agawin \nFrom BSIT-1C\nDate Created : 08/28/2024")
  print("""
  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
  \t\t\t\t\t\t\t\t\t\t\t\t\t*
  \t\t\t\t\t\t\t\t\t\t\t\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t\t\t*
  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Look Up!!
  """)

  #Code Challange 2
def code_challange2():
    print("By : Joshua Ezekiel A. Agawin\nFrom BSIT-1C\nDate Created : 08/30/2024")
    Name_code2 = input("Please enter a name ---> ")
    print("Hi", Name_code2)
    
    print("""
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    \t\t\t\t\t\t\t\t\t\t\t\t\t*
    \t\t\t\t\t\t\t\t\t\t\t\t*\t*\t*
    \t\t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*
    \t\t\t\t\t\t\t\t\t\t\t\t-----------------
    \t\t\t\t\t\t\t\t\t\t*\t\t|""","Hi!", Name_code2,"""\t|\t\t*
    \t\t\t\t\t\t\t\t\t\t\t\t-----------------
    \t\t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*
    \t\t\t\t\t\t\t\t\t\t\t\t*\t*\t*
    \t\t\t\t\t\t\t\t\t\t\t\t\t*
    \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    Look Up!!
    """)

#Code Challange 3
def code_challenge3():
    x_code3 = eval(input("enter a number: "))
    y_code3 = eval(input("enter a number: "))
    z_code3 = x_code3 + y_code3
    print(f"the sum of {x_code3} and {y_code3} is {z_code3}")
    print()

#Code Challange 4
def code_challange4():
  num1_code4 = int(input('First number : '))
  num2_code4 = int(input('Second Number : '))
  sum_code4 = num1_code4 + num2_code4
  dif_code4 = num1_code4 - num2_code4
  pro_code4 = num1_code4 * num2_code4
  quo_code4 = num1_code4 // num2_code4
  exp_code4 = num1_code4 ** num2_code4
  rem_code4 = num1_code4 % num2_code4
  flo_code4 = num1_code4 / num2_code4
  print("\nThe Sum of", num1_code4, "and", num2_code4, "is",sum_code4)
  print("The Difference of", num1_code4, "and", num2_code4, "is",dif_code4)
  print("The Product of", num1_code4, "and", num2_code4, "is",pro_code4)
  print("The Quotient of", num1_code4, "and", num2_code4, "is",quo_code4)
  print("The Exponent of", num1_code4, "by", num2_code4, "is",exp_code4)
  print("The Reminder of", num1_code4, "and", num2_code4, "is",rem_code4)
  print("The Floor Division of", num1_code4, "and", num2_code4, "is",flo_code4)
  print("\n Created By : Joshua Ezekiel A. Agawin \n Course and Section : BSIT_1C\n Date Created : 09/06/2024 (Friday) \nDate Submitted : \n Thank you!")

#Code Challange 5
def code_challange5():
    n_code5 = input("Enter Your Name : ")
    m_code5 = eval(input("Enter amount to Deposit : "))
    t_code5 = m_code5 // 1000
    t1_code5 = m_code5 % 1000
    f_code5 = t1_code5 // 500
    f1_code5 = t1_code5 % 500
    h2_code5 = f1_code5 // 200
    h21_code5 = f1_code5 % 200
    h1_code5 = h21_code5 // 100
    h12_code5 = h21_code5 % 100
    f2_code5 = h12_code5 // 50
    f21_code5 = h12_code5 % 50
    t2_code5 = f21_code5 // 20
    t21_code5 = f21_code5 % 20
    t3_code5 = t21_code5 // 10
    t31_code5 = t21_code5 % 10
    f3_code5 = t31_code5 // 5
    f31_code5 = t31_code5 % 5
    o_code5 = f31_code5 // 1
    o1_code5 = f31_code5 % 1

    print("\nHi,", n_code5, ", The breakdown of your deposit is : ")
    print(t_code5, "- 1000")
    print(f_code5, "- 500")
    print(h2_code5, "- 200")
    print(h1_code5, "- 100")
    print(f2_code5, "- 50")
    print(t2_code5, "- 20")
    print(t3_code5, "- 10")
    print(f3_code5, "- 5")
    print(o_code5, "- 1")

    print("\nCreated By : Joshua Ezekiel A. Agawin\nCourse & Section : BSIT_1C\nDate Created : 09/09/2024_Monday\nDate Submitted : 09/20/2024_Friday\nThank you!")        

#This is My Raw Code During Time of the Quiz
#name = input("Enter your name : ")
#dep = eval(input("\nEnter among to deposit : "))
#thousand = dep // 1000
#dep2 = dep - (thousand * 1000)
#five = dep2 // 500
#dep3 = dep2 - (five * 500)
#two = dep3 // 200
#dep4 = dep3 - (two * 200)
#one = dep4 // 100
#dep5 = dep4 - (one * 100)
#fifty = dep5 // 50
#dep6 = dep5 - (fifty * 50)
#twenty = dep6 // 20
#dep7 = dep6 - (twenty * 20)
#ten = dep7 // 10
#dep8 = dep7 - (ten * 10)
#five2 = dep8 // 5
#dep9 = dep8 - (five * 5)
#sin = dep9 // 1
#
#print("\nHi,", name, ", The breakdown of your deposit is : ")
#print(thousand, "- 1000")
#print(five, "- 500")
#print(two, "- 200")
#print(one, "- 100")
#print(fifty, "- 50")
#print(twenty, "- 20")
#print(ten, "- 10")
#print(five2, "- 5")
#print(sin, "- 1")

#Code Challange 6
def code_challange6():
    n_code6 = input("\nFinal Grade Computer\n\nEnter Your Name : ")
    pre_code6 = eval(input("\nPrelim Grades : "))
    mid_code6 = eval(input("Midterm Grades : "))
    sem_code6 = eval(input("Semi-Final Grades : "))
    fin_code6 = eval(input("Final Grades : "))
    qui_code6 = eval(input("Quiz Grades : "))
    pro_code6 = eval(input("Project Grades : "))

    fg_code6 = (pre_code6 * 0.15) + (mid_code6 * 0.15) + (sem_code6 * 0.15) + (fin_code6 * 0.15) + (qui_code6 * 0.25) + (pro_code6 * 0.15) 
    fg2_code6 = int(fg_code6)
    fg3_code6 = round(fg2_code6)

    if 75 <= fg_code6 <= 100 :
        print("\nCongratulations!", n_code6,", You Passed with the Final Grade of", fg3_code6)
    elif 0 <= fg_code6 <= 74:
        print("\nSorry", n_code6,", You Failed with the Final Grade of", fg3_code6)	
    else :
        print("\nInput was Invalid")

    print("\nCreated By : Joshua Ezekiel A. Agawin\nCourse & Section : BSIT_1C\nDate Created : 09/18/2024_Wednesday\nDate Submitted : 09/20/2024_Friday\nThank you!")

#Code Challange 7
total = 0
beef_rump = 0
beef_brisket = 0
pork_kasim = 0
pork_liempo = 0
whole_chicken = 0
total_payment = 0
def code_challange7():
    import datetime
    print("\nGood Day Customer!!, Welcome to Joshua's Meat Products")
    date = datetime.date.today()
    age = 0
    name = input("\nHello Customer!!, Please state your name so I can further assist you ---> ")

    def bye():
        print(f"\nCome Back again for your next Grocery!, Thank you {name}!\n")

    def list():
        print("This is the list of Meats Available as of 09-24-2024 :")
        print("\tBeef Rump = 400 php/kg\n\tBeef Brisket = 320 php/kg\n\tPork Kasim = 260 php/kg\n\tPork Liempo = 310 php/kg\n\tWhole Chicken = 180 php/kg")

    def addcart():
        global beef_rump, beef_brisket, pork_kasim, pork_liempo, whole_chicken, total
        total = 0
        beef_rump = 0
        beef_brisket = 0
        pork_kasim = 0
        pork_liempo = 0
        whole_chicken = 0
        while True:
            add = input("\nAdd to Cart the Name of the Product (or type 'done' to finish): ").lower()
            if add == "beef rump":
                total += 400
                beef_rump += 1
                tax = total * 0.123 
                final_total = total + tax
                print(f"One Kg of Beef Rump is added to the cart. Total so far: {total} + {round(tax, 2)} tax php = {final_total}")
            elif add == "beef brisket":
                total += 320
                beef_brisket += 1
                tax = total * 0.123 
                final_total = total + tax
                print(f"One Kg of Beef Brisket is added to the cart. Total so far: {total} + {round(tax, 2)} tax php = {final_total}")
            elif add == "pork kasim":
                total += 260
                pork_kasim += 1
                tax = total * 0.123 
                final_total = total + tax
                print(f"One Kg of Pork Kasim is added to the cart. Total so far: {total} + {round(tax, 2)} tax php = {final_total}")
            elif add == "pork liempo":
                total += 310
                pork_liempo += 1
                tax = total * 0.123 
                final_total = total + tax
                print(f"One Kg of Pork Liempo is added to the cart. Total so far: {total} + {round(tax, 2)} tax php = {final_total}")
            elif add == "whole chicken":
                total += 180
                whole_chicken += 1
                tax = total * 0.123 
                final_total = total + tax
                print(f"One Kg of Whole Chicken is added to the cart. Total so far: {total} + {round(tax, 2)} tax php = {final_total}")
            elif add == "done":
                break
            else:
                print("Incorrect Input, Please Try Again")
        return total

    def choice():
        choice = ""
        while choice == "":
            choice = input("Do you want to buy groceries? : [Yes/No] : "	).lower()
            if choice == "yes":
                list()
                total = addcart()
                if total == 0:
                    print(f"\nYou Didn't Buy Anything, Shop Again Next Time!, Thank you {name}!\n")
                global total_payment
                tax = total * 0.123 
                final_total = total + tax
                total_payment = 0
                while not total_payment >= final_total:
                    payment = eval(input(f"The Total will be {final_total}, Please Pay The Right Amount : "))
                    if payment < final_total:
                        total_payment += payment
                        more = total_payment - final_total
                        print(f"Please Add {abs(round(more,2))} to the Right Amount!")
                        if total_payment >= final_total:
                            change = total_payment - final_total
                            if change == 0:
                                print(f"The Grocery is Paid and you have no change, Thank you!")
                            elif change > 0:
                                print(f"The Grocery is Paid and you have {round(change)} amount of Change, Thank you!")

                    elif payment >= final_total:
                        total_payment += payment
                        change = payment - final_total
                        if change == 0:
                            print(f"The Grocery is Paid and you have no change, Thank you!")
                        elif change > 0:
                            print(f"The Grocery is Paid and you have {round(change)} amount of Change, Thank you!")
            elif choice.lower() == "no":
                exit()
                break
            else:
                choice = ""
                print("Input Error, Please Try Again!")

    def discounted_choice ():
        choice = ""
        while choice == "":
            choice = input("Do you want to buy groceries? : [Yes/No] : "	).lower()
            if choice == "yes":
                list()
                total = addcart()
                if total == 0:
                    print(f"\nYou Didn't Buy Anything, Shop Again Next Time!, Thank you {name}!\n")
                global total_payment
                tax = total * 0.123 
                final_total = total + tax
                discount = final_total - (final_total * 0.052)
                total_payment = 0
                while not total_payment >= discount:
                    payment = eval(input(f"The Total will be {round(discount, 2)}, Please Pay The Right Amount : "))
                    if payment < discount:
                        total_payment += payment
                        more = total_payment - discount
                        print(f"Please Add {abs(round(more,2))} to the Right Amount!")
                        if total_payment >= discount:
                            change = total_payment - discount
                            if change == 0:
                                print(f"The Grocery is Paid and you have no change, Thank you!")
                            elif change > 0:
                                print(f"The Grocery is Paid and you have {round(change)} amount of Change, Thank you!")

                    elif payment >= discount:
                        total_payment += payment
                        change = payment - discount
                        if change == 0:
                            print(f"The Grocery is Paid and you have no change, Thank you!")
                        elif change > 0:
                            print(f"The Grocery is Paid and you have {round(change)} amount of Change, Thank you!")    
            elif choice.lower() == "no":
                bye()
                break    
            else:
                choice = ""
                print("Input Error, Please Try Again!")

    while not age > 0 :
        age = eval(input(f"Hi {name}!, Please provide your age ---> "))
        if 0 >= age :
            print("Input Invalid, Please Try Again")
        elif 60 <= age <= 120:
            print("With Senior Discount")
            discounted_choice()
            print(f"\nJoshua's Meat Products Official Reciept\n\n{date}\n\n{beef_rump} Beef Rump : {400 * beef_rump}\n{beef_brisket} Beef Brisket : {320 * beef_brisket} \n{pork_kasim} Pork Kasim = {260 * pork_kasim}\n{pork_liempo} Pork Liempo = {310 * pork_liempo}\n{whole_chicken} Whole Chicken = {180 * whole_chicken}\n\tTotal = {total + (total * 0.123)}\n\tVATable Sales = {total}\n\tVAT Amount = {round(total * 0.123, 2)}\n\tCash = {total_payment}\n\tChange = {round(total_payment - (total + (total* 0.123)))}\n\tSenior Discount = {round((total + (total * 0.123))-((total + (total * 0.123))* 0.052), 2) }")
            bye()
        elif 1 <= age < 60:
            print("Without Discount")
            choice()
            print(f"\nJoshua's Meat Products Official Reciept\n\n{date}\n\n{beef_rump} Beef Rump : {400 * beef_rump}\n{beef_brisket} Beef Brisket : {320 * beef_brisket} \n{pork_kasim} Pork Kasim = {260 * pork_kasim}\n{pork_liempo} Pork Liempo = {310 * pork_liempo}\n{whole_chicken} Whole Chicken = {180 * whole_chicken}\n\tTotal = {total + (total * 0.123)}\n\tVATable Sales = {total}\n\tVAT Amount = {total * 0.123}\n\tCash = {total_payment}\n\tChange = {round(total_payment - (total + (total* 0.123)))}")
            bye()
            
        else:
            age = 0
            print("Input Invalid, Please Try Again!")

    #Created By Joshua Ezekiel A. Agawin From BSIT-1C | Date Created : 09-25-2024 (Wednesday) | Thank you!

    #Reference For Prices :  
    # https://www.da.gov.ph/wp-content/uploads/2024/09/Price-Monitoring-September-24-2024.pdf

#Code Challange 8
def code_challange8():
    #Summation Using For Loop
    print("Summation of ten numbers!\n\n")

    sum_code8 = 0
    odd_code8 = 0
    even_code8 = 0

    for x_code8 in range (1,11):
        no_code8 = int(input(f"Input #{x_code8}: "))
        sum_code8 += no_code8
        if no_code8 % 2 == no_code8:
            even_code8 += no_code8
        else : 
            odd_code8 += no_code8

    print(f"the summation of the number is {sum_code8}")
    print(f"the summation of the odd number is {odd_code8}")
    print(f"the summation of the even number is {even_code8}")

    print("""
    By Joshua Ezekiel A. Agawin
    From BSIT-1C
    Date Created : Oct 25, 2024
    Thank you!!    
        """)

#Code Challange 9
def code_challange9():
    Number_code9 = eval(input(f"""Inverted Mirrored Right Triangle Maker

    Enter a number: """))
    for x_code9 in range(Number_code9, 0,-1):
        for y_code9 in range(Number_code9,x_code9,-1):
            print(" ", end=" ")
        print("* " * x_code9)

    print(f"""By Joshua Ezekiel A. Agawin
    From BSIT-1C
    Date Created : 10-21-2024 (Monday)
    Date Submitted : 10-23-2024 (Wednesday)
    Credits to Andrian Marino for being the First to get the code, I learned it from him and inspired to understand it.
    Thank you!
    """)

#Code Challange 10
def code_challange10():
    for x_code10 in range (1,6):
        for y_code10 in range(6,x_code10,-1):
            print(" ",end=" ")
        for z_code10 in range(1,x_code10+1):
            print("*",end=" ")
        for a_code10 in range(1,x_code10+1):
            print("*",end=" ")
        print()

    for o_code10 in range(1,6):
        for q_code10 in range(1,o_code10+1):
            print(" ",end=" ")
        for p_code10 in range(6,o_code10,-1):
            print("*",end=" ")
        for l_code10 in range(6,o_code10,-1):
            print("*",end=" ")
        print()

    print("""
    Made by Joshua Ezekiel A. Agawin
    From BSIT-1C
    Made on 10/30/2024
    Submitted on 11/06/2024
    Thank you!    """)

#Code Challange 11
def code_challange11():
    for topleft_x_code11 in range(0,4):
        for topleft_y_code11 in range(topleft_x_code11,3):
            print(" ",end=" ")
        for topleft_y_filler_code11 in range(0,topleft_x_code11+1):
            print("*",end=" ")
        for topright_y_filler_code11 in range(0,topleft_x_code11):
            print("*",end=" ")
        print()
    for bottomleft_x_code11 in range(0,3):
        for bottomleft_y_code11 in range(0,bottomleft_x_code11+1):
            print(" ",end=" ")
        for bottomleft_y_filler_code11 in range(3,bottomleft_x_code11,-1):
            print("*",end=" ")
        for bottomright_y_filler_code11 in range (2,bottomleft_x_code11,-1):
            print("*",end=" ")
        print()

    print("""
    Made by Joshua Ezekiel A. Agawin
    From BSIT-1C
    Made on 10/30/2024
    Submitted on 11/06/2024
    Thank you!      
        """)

#Code Challange 12
def code_challange12():
    for topleft_x in range(0,5):
        for topleft_y in range(4,topleft_x,-1):
            print(" ",end=" ")
        for topleft_y_filler in range(0,topleft_x):
            print("*",end=" ")
        for topright_y_filler in range(0,topleft_x):
            print("*",end=" ")
        print()
    for bottomleft_x in range(0,4):
        for bottomleft_y in range(0,3):
            print(" ",end=" ")
        for middle_y_filler in range(0,2):
            print("*",end=" ")
        print()

    print("""
    Made by Joshua Ezekiel A. Agawin
    From BSIT-1C
    Made on 10/30/2024
    Submitted on 11/06/2024
    Thank you!      
        """)

#Code Challange 13
def code_challange13():
    for topleft_x in range(1,7):
        for topleft_y in range(6,topleft_x,-1):
            print(" ",end=" ")
        for topleft_y_filler in range (topleft_x,1,-1):
            print(topleft_y_filler,end=" ")
        for topright_y_filler in range(1,topleft_x+1):
            print(topright_y_filler,end=" ")
        print()
    for bottomleft_x in range(5,0,-1):
        for bottomleft_y in range(6-bottomleft_x,0,-1):
            print(" ",end=" ")
        for bottomeleft_y_filler in range(bottomleft_x,0,-1):
            print(bottomeleft_y_filler,end=" ")
        for bottomright_y_filler in range(2, bottomleft_x+1):
            print(bottomright_y_filler,end=" ")
        print()

    print("""
    Made by Joshua Ezekiel A. Agawin
    From BSIT-1C
    Made on 10/30/2024
    Submitted on 11/07/2024
    Thank you!      
        """)
    
#Code Challange 14
def code_challange14():
    #code_challenge14.py
    #continue to ask user for a number
    #enter number
    #loop terminates if 0
    #the sum of all the numbers given is 18.

    isLoop = True
    no = 0

    while isLoop == True:
        josh = eval(input("Enter a number> "))
        if josh > 0:
            no+= josh
            continue
        elif josh == 0:
            print("Loop has been terminated.")
            print(f"the sum of all the numbers given is {no}")
            break
            isLoop = False
        else:
            print("Please enter a number.")
            continue



    print("""By Joshua Ezekiel A. Agawin
    From BSIT-1C
    Date Created : 11/13/2024
    Date Submitted : 11/13/2024
    """)

#Code Challange 15
def code_challange15():
    #code_challenge15.py Josh
    #Hybrid Loop
    import os
    t = 1
    loop = True

    while loop == True:
        tc = input("Would you like to add a triangle? (yes / no)> ")
        if tc.lower() == "yes":
            os.system("cls")
            t += 1
            for x in range(1, 6):
                for r in range(1, t):
                    for y in range(1, x +1):
                        print("*", end=" ")
                    for z in range(6, x, -1):
                        print(" ", end=" ")
                print()
        elif tc.lower() == "no":
            os.system("cls")
            print("Program Terminated.")
            break
            loop = False
        else:
            print("Invalid input please answer only with yes or no.")
            continue

        
    print("""By Joshua Ezekiel A. Agawin
    From BSIT-1C
    Date Created : 11/13/2024
    Date Submitted : 11/13/2024
    """)

#Code Challange 16
def code_challange16():
    import os
    os.system('cls')

    #BANK SIMULATION PROGRAM 
    print(f"BANK SIMULATION PROGRAM \n\n") 

    # Filipino Denomination Breakdown Function (code from the quiz we have done )
    def denomination_breakdown(amount):
        t = amount // 1000
        t1 = amount % 1000
        f = t1 // 500
        f1 = t1 % 500
        h2 = f1 // 200
        h21 = f1 % 200
        h1 = h21 // 100
        h12 = h21 % 100
        f2 = h12 // 50
        f21 = h12 % 50
        t2 = f21 // 20
        t21 = f21 % 20
        t3 = t21 // 10
        t31 = t21 % 10
        f3 = t31 // 5
        f31 = t31 % 5
        o = f31 // 1
        o1 = f31 % 1

        print(int(t), "- 1000")
        print(int(f), "- 500")
        print(int(h2), "- 200")
        print(int(h1), "- 100")
        print(int(f2), "- 50")
        print(int(t2), "- 20")
        print(int(t3), "- 10")
        print(int(f3), "- 5")
        print(int(o), "- 1")

    # Account creation function
    def create_account():
        account_balance = 0
        print("Account created successfully!")
        return account_balance

    # Deposit function
    def deposit(account_balance):
        try:
            deposit_amount = float(input("Enter deposit amount: ₱"))
            if deposit_amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                return account_balance
            account_balance += deposit_amount
            print(f"₱{deposit_amount} deposited successfully!")
            print(f"Current Balance: ₱{account_balance}")
            denomination_breakdown(deposit_amount)
            return account_balance
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return account_balance

    # Withdraw function
    def withdraw(account_balance):
        try:
            withdraw_amount = float(input("Enter withdrawal amount: ₱"))
            if withdraw_amount <= 0:
                print("Invalid amount. Please enter a positive number.")
                return account_balance
            if withdraw_amount > account_balance:
                print("Insufficient funds.")
                return account_balance
            account_balance -= withdraw_amount
            print(f"₱{withdraw_amount} withdrawn successfully!")
            print(f"Current Balance: ₱{account_balance}")
            return account_balance
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            return account_balance

    # Check balance function
    def check_balance(account_balance):
        print(f"Current Balance: ₱{account_balance}")

    # Main function
    def main():
        account_balance = 0
        account_created = False

        while True:
            if not account_created:
                print("Welcome to the Bank Simulation Program!")
                print("1. Create Account")
            else:
                print("\nWelcome to your account!")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
            
            print("4. Exit")
            choice = input("Select an option (1-4): ")

            if choice == '1':
                os.system('cls')
                if not account_created:
                    account_balance = create_account()
                    account_created = True
                else:
                    account_balance = deposit(account_balance)
            elif choice == '2' and account_created:
                os.system('cls')
                account_balance = withdraw(account_balance)
            elif choice == '3' and account_created:
                os.system('cls')
                check_balance(account_balance)
            elif choice == '4':
                print("Thank you for using the Bank Simulation Program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    if __name__ == "__main__":
        main()

    print("""
    By Joshua Ezekiel A. Agawin
    From BSIT-1C
    Date Created : 11/18/2024 (Monday)
    Thank you!
        """)

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
                            activity4()
                        elif print_choose == "4":
                            print("code_challange1.py \n")
                            code_challange1()
                        elif print_choose == "5":
                            print("code_challange2.py\n")
                            code_challange2()
                        elif print_choose == "6":
                            print("code_challange4.py\n")
                            code_challange4()
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
                            activity3()
                        elif variables_choose == "2":
                            while True:
                                print("activity24.py \n")
                                activity24()
                                break
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
                                        activity4()
                                    elif arithmetic_operators_choose == "2":
                                        print("activity5.py \n")
                                        activity5()
                                    elif arithmetic_operators_choose == "3":
                                        print("code_challange3.py \n")
                                        code_challenge3()
                                    elif arithmetic_operators_choose == "4":
                                        print("code_challange4.py\n")
                                        code_challange4()
                                    elif arithmetic_operators_choose == "5":
                                        print("code_challange5.py \n")
                                        code_challange5()
                                    elif arithmetic_operators_choose == "6":
                                        print("code_challange7.py \n")
                                        code_challange7()
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
                                        activity6()
                                    elif assignment_operators_choose == "2":
                                        print("code_challange7.py\n")
                                        code_challange7()
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
                                        activity7()
                                    elif comparison_operators_choose == "2":
                                        print("activity9.py \n")
                                        activity9()
                                    elif comparison_operators_choose == "3":
                                        print("code_challange6.py\n")
                                        code_challange6()
                                    elif comparison_operators_choose == "4":
                                        print("code_challange7.py")
                                        code_challange7()
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
                                        activity9()
                                    elif logical_operators_choose == "2":
                                        print("activity10.py \n")
                                        activity10()
            
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
                            activity7()
                        elif conditionals_choose == "2":
                            print("activity9.py\n")
                            activity9()
                        elif conditionals_choose == "3":
                            print("activity10.py")
                            activity10()
                        elif conditionals_choose == "4":
                            print("code_challange6.py\n")
                            code_challange6()
                        elif conditionals_choose == "5":
                            print("code_challange7.py \n")
                            code_challange7()
                
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
                                        activity11()
                                    elif for_loop_choice == "2":
                                        print("activity12.py \n")
                                        activity12()
                                    elif for_loop_choice == "3":
                                        print("activity13.py \n")
                                        activity13()
                                    elif for_loop_choice == "4":
                                        print("activity14.py \n")
                                        activity14()
                                    elif for_loop_choice == "5":
                                        print("activity15.py \n")
                                        activity15()
                                    elif for_loop_choice == "6":
                                        print("activity16.py \n")
                                        activity16()
                                    elif for_loop_choice == "7":
                                        print ("activity17.py \n")
                                        activity17()
                                    elif for_loop_choice == "8":
                                        print("activity18.py \n")
                                        activity18()
                                    elif for_loop_choice == "9":
                                        print("code_challange8.py \n")
                                        code_challange8()
                                    elif for_loop_choice == "10":
                                        print("code_challange9.py \n")
                                        code_challange9()
                                    elif for_loop_choice == "11":
                                        print("code_challange10.py\n")
                                        code_challange10()
                                    elif for_loop_choice == "12":
                                        print("code_challange11.py \n")
                                        code_challange11()
                                    elif for_loop_choice == "13":
                                        print("code_challange12.py \n")
                                        code_challange12()
                                    elif for_loop_choice == "14":
                                        print("code_challange13.py")
                                        code_challange13()
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
                                        activity19()
                                    elif while_loop_choice == "2":
                                        print("code_challange14.py \n")
                                        code_challange14()
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
                                        activity20()
                                    elif hybrid_loop_choice == "2":
                                        print("code_challange15.py \n")
                                        code_challange15()
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
                            activity25()
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
                            while True:
                                activity8_menu()
                                activity8_choice = input("Choose a Command : ")
                                if activity8_choice == "0":
                                    os.system('cls')
                                    break
                                elif activity8_choice != "0":
                                    os.system('cls')
                                    if activity8_choice == "1":
                                        create_user()
                                        continue
                                    elif activity8_choice == "2":
                                        login()
                                        continue
                                else:
                                    print("Invalid Command, Try Again!")
                        elif function_choice == "2":
                            print("activity21.py \n")
                            activity21()
                        elif function_choice == "3":
                            print("activity23.py \n")
                            number_act23 = eval(input("Enter a number : "))
                            activity23(number_act23)
                            print(f"the factorial of number {number_act23} is {activity23(number_act23)}")
                        elif function_choice == "4":
                            print("code_challange16.py \n")
                            code_challange16()

                
                        
                    

#Print Statements Menu
def print_statement():
    print("""
+----------------------------------------------------------------+      
|                    [1] Print Statements                        |
+----------------------------------------------------------------+
| > The print() statement is used to output data to the console  |
| > One of the most commonly used built-in functions             |
| > Use the Activites and Code Challange for Example (1 - 6)     |                    
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
+----------------------------------------------------------------+
| > Variable is a symbolic name that reference or points to a    |
| value stored in memory.                                        |
| > Variable makes it easy to work with data                     |
| > Use the Activities for example (1 - 2)                       |                    
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity3.py            |                                  |
| (2) activity24.py           |                                  |          
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
| > Operators are used to perform operations on variables and    |
| values.                                                        |
| > Python supports several types of operators                   |
| > Which you can choose between this four (1 - 4)               |          
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
+----------------------------------------------------------------+
| > Used for Mathematical Calculations                           |
| > Examples are [+ Addition], [- Subtraction], [/ Division],etc.|
| > Use the Activities and Code Challange for Example (1 - 6)    |          
+----------------------------------------------------------------+                    
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
+----------------------------------------------------------------+
| > Used to Assign Values to Variables                           |
| > Examples are [= Assign], [+= Add and Assign], etc.           |
| > Use the Activity and Code Challange for Example (1 - 2)      |
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
+----------------------------------------------------------------+
| > Used to compare two values, returning True or False          |
| > Examples are [== Equal to], [!= Not Equal to], etc.          |
| > Use the Activities and Code Challanges for Example (1 - 4)   |
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
+----------------------------------------------------------------+
| > Used to combine conditional statements.                      |
| > Examples are [and], [or], & [not]                            |
| > Use the Activities for Example (1 - 2)                       |                 
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
+----------------------------------------------------------------+
| > Controls the flow of the program based on the conditions     |
| > Examples are [if], [elif], [else]                            |
| > Use the Activities and Code Challanges for Example (1 - 5)   | 
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
| > Used to repeat a block of code multiple times                |
| > Examples are [for], [while], & [hybrid]                      |
| > Which you can explore by choosing between the three (1 - 3)  |
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
+----------------------------------------------------------------+
| > Iterate over a sequence (e.g., a list, tuple, dict., etc.)   |
| > Execute a block of code for each element in the sequence     |
| > Use the Activities and Code Challanges for Example (1 - 14)  |
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
+----------------------------------------------------------------+
| > Repeats a block of code as long as specified condition is    |
| True.                                                          |
| > Use the Activity and Code Challange for Example (1 - 2)      |
+----------------------------------------------------------------+          
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
+----------------------------------------------------------------+
| > Refers to combining elements of different loop types         |
| > Combination of [for] and [while]                             |
| > Use the Activity for Example (1)                             |
+-----------------------------+----------------------------------+          
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity20.py           | (2) code_challange15.py          |                                        
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Loops Menu                                      |
+-----------------------------+----------------------------------+          
      """)

#list menu
def list():
    print("""
+----------------------------------------------------------------+      
|                      [6] Lists                                 |
+----------------------------------------------------------------+
| > Data Structure used to store collection of items             |
| > Mutable, Ordered, and allow duplicate elements               |
| > Use the Activity for Example (1)                             |  
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
+----------------------------------------------------------------+
| > Reusable blocks of code that perform a specific task         |
| > Help organize and structure code, making it modular          |
| , readable, and maintainable.                                  |
| > Use the Activities and Code Challange for example (1 - 3)    |  
+-----------------------------+----------------------------------+        
|         Activities          |          Code Challange          |
+-----------------------------+----------------------------------+                                                              
| (1) activity8.py            | (4) code_challange16.py          |                                        
| (2) activity21.py           |                                  |  
| (3) activity23.py           |                                  |                                                
+-----------------------------+----------------------------------+                                                             
| (0) Go Back to Main Menu                                       |
+-----------------------------+----------------------------------+          
      """)            

def exit():
    os.system('cls')
    print(f"Thank you for using the Program! Have a Great Day {user}!")

main()
