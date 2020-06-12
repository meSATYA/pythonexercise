#!/usr/bin/python

w = int(input("Please enter first number: "))
x = int(input("Please enter second number: "))
y = int(input("Please enter third number: "))
z = int(input("Please enter fourth number: "))

res=0

if (w >= x) and (w >= y) and (w >= z):
    print(w, "is the biggest number");
    res=w;
elif (x >= w) and (x >= y) and (x >= z):
    print(x,"is the biggest number");
    res=x;
elif (y >= w) and (y >= x) and (y >= z):
    print(y,"is the biggest number");
    res=y;
else:
    print(z, "is the biggest number");
    res=z;
	
p = int(input("Please enter fifth number: "))

if(res<p):
    print("The biggest number is: ", p)
else:    
	print("The biggest number is: ", res)
