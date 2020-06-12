#!/usr/bin/python

x = int(input('Enter First number : '))
y = int(input('Enter Second number : '))
z = int(input('Enter Third number : '))
def largest(a, b, c):
    if (a > b) and (a > c):
        largest = a
    elif (b > a) and (b > c):
        largest = b
    else:
        largest = c
    print("The largest of the 3 numbers is : ", largest)
def smallest(a, b, c):
    if (a < b) and (a < c):
        smallest = a
    elif (b < a) and (b < c):
        smallest = b
    else:
        smallest = c
    print("The smallest of the 3 numbers is : ", smallest)
	
largest(x, y, z)
smallest(x, y, z)