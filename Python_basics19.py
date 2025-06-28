# Exercise: 19: Print Alternate Prime Numbers till 20
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17

prime_list=[]
for i in range(2,21):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_list.append(i)

print(prime_list)
#print all of them in list
for i in prime_list:
    print(i,end=" ")
#printing alternate ones by using slicing method
print()
for i in prime_list[::2]:
    print(i,end=" ")
print()
#printing alternate ones by using counter method

c=0
for i in prime_list:
    if c%2!=0:
        print(i,end=" ")
