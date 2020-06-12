#!/usr/bin/python

list1 = [100,101,102,103,104,105,106,107,108,109]
list2 = ["Rajnikant","Aishwariya","Shahrukh","Kajol","Salman","Katrina","Ranvir","Deepika","Ayushman","Kriti"]

print("Name of the employees are: ",list2)
x = int(input("Please provide the index number(0 is the first and 9 is the last): "))
print("Respective employee is:", list2[x], "with employee id:",list1[x])
print("Name of the employees from 04th position to 09th position are: ",list2[3:9])
print("Name of the employees from 04th position to 09th position are: ",list2[2:10])

y = int(input("Please provide how many times you want to repeat the employee names: "))

print(list2*y)

print("Concatenation of two lists: ", list1+list2)

print("Now printing lists of empoyee and their names: \n")
for i in range(0,10):
    print(list1[i],list2[i],"\n")


