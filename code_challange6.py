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