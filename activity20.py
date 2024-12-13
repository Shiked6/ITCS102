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
