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