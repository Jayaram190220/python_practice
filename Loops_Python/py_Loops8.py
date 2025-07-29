#Exercise 8: Print list in reverse order using a loop

# list1 = [10, 20, 30, 40, 50]
# rev_list=reversed(list1)
# for i in list1[::-1]:
#     print(i)

def list1(*num):
    list2=[]
    for i in num[::-1]:
        list2.append(i)
    return list2
a=list1(10, 20, 30, 40, 50)

# print(a)

for i in a:
    print(i)
