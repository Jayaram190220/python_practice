#Exercise 15: Print elements from a given list present at odd index positions

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#
# for i in my_list[1::2]:
#     print(i,end=' ')

def odd_index(*my_list):
    new_list=[]
    for i in my_list[1::2]:
        new_list.append(i)
    return new_list

a=odd_index(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
# print(a)

for i in a:
    print(i,end=" ")
