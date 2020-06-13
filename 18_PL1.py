#!/usr/bin/python

flag = int(input("Please enter '1' to print (1-100) OR '0' to print (100-1):\n"))

print("Inside for loop\n")
for i in range(1,101):
    if(flag==1):
        print("In ascending order: ",i,"\n")
    else:
        print("In descending order order: ",101-i,"\n")

j=1
print("Inside While loop\n")
while (j>0) & (j<101):
    if(flag==1):
        print("In ascending order: ",j,"\n")
    else:
        print("In descending order order: ",101-j,"\n")
    j+=1

mystring ="Hello World"

print("Printing charcters of Hello World string")
for k in range(0,len(mystring)):
    print(mystring[k])    