year=int(input("please type in a year:"))

if (year%4==0) :
   print("that year is a leap year.")
elif(year%100)and(year%400):
   print("that year is a leap year.")
else:
   print("that year is not a leap year.")