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