total=int(input("total amount:"))
item=int (input("number of items:"))
day=str(input("day of the week:"))
weekday=['monday','tuesday','wednesday','thursday','friday']
weekends=['saturday','sunday']

if (item>5):
 total-=total*0.05

if(day in weekday):
  total-=total*0.1
elif(day in weekends):
  total-= total*0.2

print("total price after discount:",total)