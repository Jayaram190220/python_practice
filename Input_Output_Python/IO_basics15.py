#Exercise 15: Padding with Zeros

num=int(input("enter number:"))
num_str=str(num)
b=5-len(num_str)
print("0"*b+num_str)
