#Exercise 9: Display numbers from -10 to -1 using for loop

# for i in range(-10,0,1):
#     print(i)

def display_numbers(n):
    lis1=[]
    for i in range(-n,0,1):
        lis1.append(i)
    return lis1

a=display_numbers(10)

# print(a)

for i in a:
    print(i)
