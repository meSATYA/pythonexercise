#!/usr/bin/python

x = int(input("Please enter a number: "))

r = x%2

if (r==0):
    print(x, "is even")
else:
    print(x, "is odd")