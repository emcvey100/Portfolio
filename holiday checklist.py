#Write a program that allows the user to create and store a checklist for a holiday.
#It should start by asking them the destination of the holiday, how many things they need to pack and how many tasks they need ti complete to prepare.
#The user should then be able to enter each item they need to pack and each task they need to complete.

packing=[]
tasks=[]

name = input("Name:")
num=int(input("Number of items:"))
for i in num:
    packing.append(input("Item:"))
num=int(input("Number of tasks:"))
for i in num:
    tasks.append(input("Tasks:"))
file=open((name+" checklist.txt"), "w")
file.write("Desitnation: "+name+"\nPacking List: \n")
for item in packing:
    file.write(item+"\n")
file.write("Tasks: \n")
for i in tasks:
    file.write(i+"\n")
    
