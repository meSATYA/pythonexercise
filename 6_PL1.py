#!/usr/bin/python

x = str(input("Please input first string: "))

for i in range(0,len(x)): 
    print("String Element #",i+1,"=",x[i]);
    print("\n") 

print("slicing the string: ", x[1:3])

print("the string is getting printed 100 times: \n")
print("\n", x*100)

y = str(input("Please input second string: "))

print("after concatenating two strings: ", x+y)
