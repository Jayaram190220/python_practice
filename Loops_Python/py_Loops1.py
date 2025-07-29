#Exercise 1: Print first 10 natural numbers using while loop

# num=1
# while num<=10:
#     print(num)
#     num=num+1


def natural(n):
    empty_list=[]
    cntr=0
    while cntr<=n:
        cntr=cntr+1
        empty_list.append(cntr)
    return empty_list

a=(natural(9))

for i in a:
    print(i)
