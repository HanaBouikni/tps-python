x=int(input("How many people need a ride? "))
y=int(input("How many people can feet in one taxi? "))

z=x//y
if (x % y!=0):
    z+=1

print("number of taxis needed:",z)


  
  

