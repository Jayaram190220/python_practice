#Exercise 13: Find the factorial of a given number

num=int(input('enter number'))

factorial=1

for i in range(1,num+1):
    factorial=factorial*i
print(factorial)

