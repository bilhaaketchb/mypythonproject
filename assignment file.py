#create a python to check if the years is leap or
#LEAP YEAR IS DIVISIBLE BY 4 BUT NOT DIVISIBLE BY 100
#EXCEPT IF ITS ALSO DISIBLE BY 400

year=int(input("enter year:"))
if year % 4==0 and (year%100!=0 or year%400==0):
    print(year,"is a leap year")
else:
    print(year,"Is not a leap Year")