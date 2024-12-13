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