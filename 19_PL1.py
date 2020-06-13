#!/usr/bin/python


print("Inside for loop\n")
for i in range(1,101):
    if(i%2==0) and (i<=51):
        print("Even Number: ",i,"\n")
        continue

j=1        
print("Inside While loop\n")
while (j>0) & (j<101):
    if(j%2==0) and (j<=51):
        print("Even Number: ",j,"\n")
    j+=1
    continue
            