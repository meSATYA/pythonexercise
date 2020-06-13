#!/usr/bin/python

a=int(input("Enter the elements: "))
f=0                                       
s=1
if a<=0:
    print("The requested series is: ",f)
else:
    print("Fibonacci series is: ",f,s,end=" ")
    for x in range(2,a-1):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next