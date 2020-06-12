#!/usr/bin/python

x = int(input("Please enter a number: "))
y = int(input("Please enter second number: "))

print("Bitwise AND Operation: ", x&y)
print("Bitwise OR Operation: ", x|y)
print("Bitwise XOR Operation: ", x^y)
print("Bitwise NOT Operation for first number: ", ~x)
print("Bitwise Left Shift Operation for first number: ", x << 2)
print("Bitwise Right Shift Operation for first number: ", x >> 2)
