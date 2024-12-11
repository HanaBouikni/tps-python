print("Runner 1 :")
name1=str(input("Name:"))
time1=float(input("Time (in seconds):"))
print("Runner 2 :")
name2=str(input("Name:"))
time2=float(input("Time (in seconds):"))

if(time1>time2):
    print("The faster runner is ",name1)
elif(time1<time2):
    print("The faster runner is ",name2)
else:
    print(name1,"and",name2,"have same time")