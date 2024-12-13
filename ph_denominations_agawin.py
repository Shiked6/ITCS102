n = input("Name : ")
m = eval(input("Money : "))

t = m // 1000
t1 = m % 1000
f = t1 // 500
f1 = t1 % 500
h2 = f1 // 200
h21 = f1 % 200
h1 = h21 // 100
h12 = h21 % 100
f2 = h12 // 50
f21 = h12 % 50
t2 = f21 // 20
t21 = f21 % 20
t3 = t21 // 10
t31 = t21 % 10
f3 = t31 // 5
f31 = t31 % 5
o = f31 // 1
o1 = f31 % 1

print(t, "- 1000")
print(f, "- 500")
print(h2, "- 200")
print(h1, "- 100")
print(f2, "- 50")
print(t2, "- 20")
print(t3, "- 10")
print(f3, "- 5")
print(o, "- 1")