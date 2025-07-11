#Exercise 6: Count the total number of digits in a number

num=75869
cnt=0
while num>0:
    num=num//10
    cnt=cnt+1
print(cnt)
