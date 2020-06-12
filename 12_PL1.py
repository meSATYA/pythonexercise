#!/usr/bin/python

list1 = []
y=0
j=0

print("Please input 10 numbers: ")

for i in range(0,10):
    x = int(input())
    list1.append(x)
    y+=x
    
avg=y/10

print("Ten numbers are: ", list1)
print("average of ten numbers is: ",avg)

for k in range(0,10):
    if(list1[k]>avg):
        j+=1
print(j,"numbers are more than average")

eq =0

for k in range(0,10):
    if(list1[k]==avg):
        eq+=1
print(eq,"numbers are equal to average")

