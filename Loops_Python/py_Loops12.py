#Exercise 12: Display Fibonacci series up to 10 terms

# num1, num2 = 0, 1
# sm = 0
# for i in range(10):
#     print(num1, end=' ')
#     sm = num1 + num2
#     num1 = num2
#     num2 = sm


def fibbonaci(n):
    num1, num2 = 0, 1
    sm = 0
    for i in range(n):
        print(num1, end=' ')
        sm = num1 + num2
        num1 = num2
        num2 = sm
