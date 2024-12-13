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