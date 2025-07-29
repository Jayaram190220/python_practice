#Exercise 10: Display a message “Done” after the successful execution of the for loop

# for i in range(5):
#     print(i)
#
# print('Done!')

def succesful(n):
    new_list=[]
    for i in range(n):
        new_list.append(i)
    return new_list

a=succesful(5)
# print(a)

for i in a:
    print(i)


print('Done!')
