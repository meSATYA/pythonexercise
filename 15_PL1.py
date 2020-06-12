#!/usr/bin/python

list1 = ["John", "Harry", "Sejal", "Robert", "Gimeso"]

y = str(input("Please enter a name: "))

for i in list1:
    if(i==y):
        print("Name is present\n")
    else:
        print("Name is not present\n")
        
print("Trying with non membership method: ")        
k=0      
while k < len(list1):
    if(list1[k]==y):
        print("Name is present\n")
    else:
        print("Name is not present\n")
    k+=1        
list1.reverse()
print("In reverse order: ",list1)    