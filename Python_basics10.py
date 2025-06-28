# Exercise 10: Merge two lists using the following condition
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

result_List=[]

for i in list1:
    if i%2!=0:
        result_List.append(i)
for i in list2:
    if i%2==0:
        result_List.append(i)
print(result_List)
