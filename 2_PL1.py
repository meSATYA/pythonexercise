#!/usr/bin/python

x = int(input("Please enter first number: "))
y = int(input("Please enter second number: "))
z = int(input("Please enter third number: "))

if (x >= y) and (x >= z):
    print(x, "is the biggest number")
elif (y >= x) and (y >= z):
    print(y,"is the biggest number")
else:
    print(z, "is the biggest number")