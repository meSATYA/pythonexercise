#!/usr/bin/python

x = int(input("Please enter a number: "))

if x > 1:
   
   for i in range(2,x):
       if (x % i) == 0:
           print(x,"is not a prime number")
           break
   else:
       print(x,"is a prime number")
       
else:
   print(x,"is not a prime number")

print("Prime numbers in between 1 to",x,"are:")   
for a in range(2,x+1):
    k=0
    for i in range(2,a//2+1):
        if(a%i==0):
            k=k+1
    if(k<=0):
        print(a)