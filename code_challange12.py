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