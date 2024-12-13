col = eval(input("Enter number of column : "))

for x in range(1,11):
    for y in range(1,col+1):
        print(f"{x*y}",end="\t")
    print()