#Exercise 12: Calculate income tax

income=45000
original=income
if original>10000:
    income=income-10000
if original<20000 and original>10000:
    tax=income*0.10
    print("tax:",tax)
elif original>20000:
    taxx=income-10000
    sam=(taxx*0.20)+(10000*0.10)
    print("tax:",sam)
else:
    print("no tax")
