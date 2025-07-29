#Exercise 3: Calculate sum of all numbers from 1 to a given number

#
# n=int(input('Enter number'))
# sm=0
# for i in range(1,n+1):
#     sm=i+sm
# print(sm)

def sum_number(num):
    sm=0
    for i in range(1,num+1):
        sm=i+sm
    return sm

a=sum_number(10)

print(a)


