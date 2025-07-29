#Exercise 11: Print all prime numbers within a range

# start=25
# end=50
#
# for i in range(start,end+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

def prime_number(start,end):
    prime_list=[]
    for i in range(start,end+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime_list.append(i)
    return prime_list

a=prime_number(25,50)

# print(a)
print("Prime numbers between 25 and 50 are:")
for i in a:
    print(i)
