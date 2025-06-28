# Exercise 18: Check if a given year is a leap year
Year2=2001
if (Year2%4==0) and (Year2%100!=0 or Year2%400==0):
    print("LEAP YEAR")
else:
    print("Not a leap year")

