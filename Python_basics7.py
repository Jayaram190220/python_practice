# Exercise 7: Find the number of occurrences of a substring in a string

str_x = "Emma is good developer. Emma is a writer"

wrd=""
empty_list=[]
for i in str_x:
    if i not in [" ","."]:
        wrd=wrd+i
    if i in [" "]:
        empty_list.append(wrd)
        wrd=""
empty_list.append(wrd)
print(empty_list)

cntr={}

for i in empty_list:
    if i in cntr:
        cntr[i]+=1
    if i not in cntr:
        cntr[i]=1
print(cntr)

numbers_list=[]

for i in cntr:
    numbers_list.append(cntr[i])
print(numbers_list)

numbers_list=sorted(numbers_list,reverse=True)

for i in numbers_list:
    for key,val in cntr.items():
        if i==val:
            print(i,key)
            numbers_list.remove(i)

