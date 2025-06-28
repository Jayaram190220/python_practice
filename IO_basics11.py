#Exercise 11: Percentage Display

number=float(input())
denominator=float(input())
if denominator<=0:
    print("denominator should not be zero")
else:
    c=((number/denominator)*100)
    print(f"The percentage:{c:.2f}%")
