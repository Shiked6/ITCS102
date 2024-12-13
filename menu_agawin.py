# Objective: Develop a comprehensive text-based program in Python that serves as an interactive menu allowing users to navigate through multiple topics covering fundamental concepts such as print statements, variables, operators, conditionals, loops, lists, and functions. The program should provide a structured environment for learning and experimenting with Python fundamentals. 

def act1():
  print("Typing Test")

def act2():
  Name = input("What is your name? ")
  print("Hi", Name, "Good afternoon")

def act2():
def act3():
  
def act4(): 
  num1 = eval(input("Enter a number ---> "))
  num2 = eval(input("Enter another number ---> "))
  sum = num1 + num2
  print("The sum of" , num1,"and", num2,"is", sum)
  
def act5():
  print("Fahrenheit to Celsius Converter Program\n\nFormula used : C = (F - 35) * 5 / 9")
  temp = eval(input("\nEnter temperature in Fahrenheit : "))
  cel = temp - 32
  cel2 = cel * 5
  cel3 = cel2 / 9
  cel4 = round(cel3, 2) 
  print("The Conversion of",temp ," degrees Fahrenheit is ",cel4 , "degrees Celsius.")
  print("\nCreated By : Joshua Ezekiel A. Agawin\nCourse and Section : BSIT_1C\nDate Created : 09/11/2024 (Wednesday)\n Thank you!")

def act6():
  x = 5
  print(x)
  #Updating the Value of x
  x = x + 10
  print(x)
  x = x + 15
  print(x)
  #simplified version
  x += 20
  print(x)
  #other arithmetic
  x -= 25
  print(x)
  
  print("\nBy Joshua Ezekiel A. Agawin,\nFrom BSIT_1C\nDate Created : 09/16/2024\nThank you!")
  
def act7():
  miner = input("Please put your name --> ")
  gold = 0
  miner_action = input("Did you mine any gold today? Yes or No? ")
  
  if miner_action.lower() == "yes" :
  	gold += 1
  	print(f"Hi {miner}, Today you have a total of {gold} gold")
  elif miner_action.lower() == "no" :
  	print(f"Hi {miner}, Today you have a total of {gold} gold")
  else :
  	print("You have type a different word that is not yes or no.. Try Again..")
  
  print("\nBy Joshua Ezekiel A. Agawin,\nFrom BSIT_1C\nDate Created : 09/16/2024\nThank you!")

def act8():
  todo = eval(input("Press 1 for Login and Press 2 to Register : "))
  def thepass() :
  	w = open("username.txt","r")
  	w = w.read()
  	password = input("Welcome!", w, "Enter your password ---> ")
  	f = open("password.txt","r")
  	f = (f.read())
  	if password == f :
  		print("You are now Logged in\nEnjoy Using the System!")
  	else :
  		print("Password Incorrect, Try Again")
  
  def register() :
  	user = input("Create Username : ")	
  	x = open("username.txt","w")
  	x.write(user)
  	x.close
  
  if todo == 1:
  	thepass()
  elif todo == 2 :
  	register()
  else :
  	print("No Action Done")
  
  
  print("\n Thank you!")
  
def act9():
  a = eval(input("Age Bracket Determiner \nEnter Age : "))
  
  if 1 <= a <= 7 :
  	print("Toddler")
  elif 8 <= a <= 13 :
  	print("Pre Teen")
  elif 14 <= a <= 18 :
  	print("Teenager")
  elif 19 <= a <= 31 :
  	print("Early Adulthood")
  elif 32 <= a <= 45 :
  	print("Mid Adulthood")
  elif 46 <= a <= 59 :
  	print("Post Adulthood")
  elif 60 <= a <= 150:
  	print("Senior")
  else :
  	print("Invalid Age")
  
  print("\nMade By : Joshua Ezekiel A. Agawin \nFrom : BSIT-1C\nDate Created : 09/20/2024\n Thank You!")

def act10():

def act11():
  #Print Hello world 10 times
  
  for x in range(1, 11):
      print(x,"Hello World!")

def act12():
  #Try the following values :
  #Starting Point is 10
  #Stopping Point is 1
  #What would be the output of the following value?
  
  for cycle in range(10,0,-1):
      print(cycle)
    
def act13():
  #Factorial = 1
  #Enter any Number : 
  
  print(f"Factorial Calculator\n")
  
  factorial = eval(input("Enter any number to Factor : "))
  result = 1
  for x in range(factorial,0,-1):
      result *= x
      
  print(f"The Factorial of {factorial} is {result}")
  print(f"""
  Created By : Joshua Ezekiel A. Agawin
  From BSIT-1C
  Date Created : 10/16/2024
  Thank you!""")
  
def act14():
  for x in range(0,11):
      print(x, end=" ")
      for y in range(0,11):
          print(" ❤️ ",end="")
      print()
  
  print("For Sir Mesiera")
  
  print(f"""Made by Joshua Ezekiel A. Agawin
  From BSIT-1C
  Made on 10-21-2024 (Monday)
  Thank you!
  """)
  
def act15():
  
def act16():

def act17():
  col = eval(input("Enter number of column : "))
  
  for x in range(1,11):
      for y in range(1,col+1):
          print(f"{x*y}",end="\t")
      print()
    
def act18():
  tri = eval(input("Enter number of triangles : "))
  
  for x in range(1,5):
      for  r in range(1,tri+1):
          for y in range(1,x+1):
              print("*",end=" ")
          
          for z in range(5,x,-1):
              print(" ",end=" ")
      print()
    
def act19():
  name = input("Enter your name : ")
  hi = input
  while
def act20():
  import os
  
  iscontinue = True
  tri = 0
while iscontinue == True:
    ask = input("Would you like to add another trianle [yes/no] --> ")
  
      if ask.lower() == "no":
          print("PROGRAM GO BOOM")
          break
          iscontinue = False
      elif ask.lower() =="yes":
          os.system('cls')
          tri += 1
          for x in range(1,5):
              for  r in range(1,tri+1):
                  for y in range(1,x+1):
                      print("*",end=" ")
           
                  for z in range(5,x,-1):
                      print(" ",end=" ")
              print()
          continue

def act21():
  print(f"Compilation of All, Like This Code")

def code1():
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
  """)

def code2():
  print("By : Joshua Ezekiel A. Agawin\nFrom BSIT-1C\nDate Created : 08/30/2024")
  Name = input("Please enter a name ---> ")
  print("Hi", Name)
  
  print("""
  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
  \t\t\t\t\t\t\t\t\t\t\t\t\t*
  \t\t\t\t\t\t\t\t\t\t\t\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t\t-----------------
  \t\t\t\t\t\t\t\t\t\t*\t\t|""","Hi!", Name,"""\t|\t\t*
  \t\t\t\t\t\t\t\t\t\t\t\t-----------------
  \t\t\t\t\t\t\t\t\t\t\t*\t*\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t\t*\t*\t*
  \t\t\t\t\t\t\t\t\t\t\t\t\t*
  \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
  """)
  
def code3():
def code4():
  num1 = int(input('First number : '))
  num2 = int(input('Second Number : '))
  sum = num1 + num2
  dif = num1 - num2
  pro = num1 * num2
  quo = num1 // num2
  exp = num1 ** num2
  rem = num1 % num2
  flo = num1 / num2
  print("\nThe Sum of", num1, "and", num2, "is",sum)
  print("The Difference of", num1, "and", num2, "is",dif)
  print("The Product of", num1, "and", num2, "is",pro)
  print("The Quotient of", num1, "and", num2, "is",quo)
  print("The Exponent of", num1, "by", num2, "is",exp)
  print("The Reminder of", num1, "and", num2, "is",rem)
  print("The Floor Division of", num1, "and", num2, "is",flo)
  print("\n Created By : Joshua Ezekiel A. Agawin \n Course and Section : BSIT_1C\n Date Created : 09/06/2024 (Friday) \nDate Submitted : \n Thank you!")

def code5():
def code6():
  print("Final Grade Computer")
  pre = eval(input("Enter your Prelim Grade ---> "))
  mid = eval(input("Enter your Midterm Grade ---> "))
  sem =  eval(input("Enter your Semi-Final Grade ---> "))
  fin = eval(input("Enter your Final Grade ---> "))
  qui = eval(input("Enter your Quiz Grade ---> "))
  pro = eval(input("Enter your Project Grade---> "))
  
  fg = (pre * 0.15) + (mid * 0.15) + (sem * 0.15) +(fin * 0.15) +(qui * 0.25) +(pre * 0.15)
  
  if fg >= 75 :
  	print("You Passed the course with your final grade being", fg)
  else :
  	print("Sorry, You Failed with the final grade of", fg)
    
def code7():
def code8():
  #Fetch 10 random numbers from the users. After acquiring all the numbers, get the summation at all the provided numbers
  # print("Summation of 10 Random Numbers\n")
  # x = 0
  # for z in range (1,11) :
  #     add = eval(input(f"Input #{z} = "))
  #     x += add
  
  # print(f"\nThe Summation of the 10 random numbers is : {x}")
  
  # print("\nBy Joshua Ezekiel A. Agawin\nFrom BSIT-1C\nCreated on : 10-14-2024(Monday)\nThank you!\n")
  
  print("Summation of 10 Random Numbers\n")
  x = 0
  odd = 0
  even = 0
  for z in range (1,11) :
      add = eval(input(f"Input #{z} = "))
      x += add
      if add % 2 == 0:
          even += add
      else:
          odd += add
  
  print(f"""\nThe Summation of the 10 random numbers is : {x}
  The summation of the even numbers is : {even}
  The summation of the odd numbers is : {odd}
  """)
  
def code9():
  for x in range(1,6):
    for y in range(1,x+1):
        print(" ",end=" ")
    for z in range(6,x,-1):
        print("*",end=" ")
    print()
    
def code10():
  for x in range(1,6):
      for y in range(1,6):
          print("*",end="")
      print()         
      
def code11():
  for x in range(1,5):
      #decrement
      for y in range(4,x,-1):
          print(" ",end=" ")
      #increment
      for z in range(1,x+1):
          print("*",end=" ")
      for a in range(1,x+1):
          print("*",end=" ") 
      print()
    
def code12():
  for x in range(1,5):
      #decrement
      for y in range(4,x,-1):
          print(" ",end=" ")
      #increment
      for z in range(1,x+1):
          print("*",end=" ")
      for a in range(1,x+1):
          print("*",end=" ") 
      print()
  for gap in range(1,5):
      for space in range(0,6):
          print(" ",end="")
      for middle in range(0,2):
          print("*",end=" ")
      print()
  
  print(f"""
  By Joshua Ezekiel A. Agawin
  From BSIT-1C
  Made on 10-30-2024(Wednesday)
  Thank you!
  """)
  
def code13():
def code14():
def code15():
def code16():
  number1 = 10
  number2 = 10
  
  def sum_no(number1,number2):
      return number1 + number2
  
  print(sum_no(number1,number2))
  
  print("""
  By Joshua Ezekiel A. Agawin
  From BSIT-1C
  Date Created : 11/15/2024(Friday)
  Thank you!
  """)



