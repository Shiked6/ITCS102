name = input("Enter your Name : ")
num = eval(input("Enter the Number : "))
even = num % 2
five = num % 5
if even == 0:
	print("Good Day",name,"\b!, The Number",num,"is an Even Number")
	
else:
	print("Good Day",name,"\b!, The Number",num,"is an Odd Number")