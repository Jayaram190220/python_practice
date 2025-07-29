#Exercise 5: Display numbers from a list using a loop

# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in numbers:
#     if i>500:
#         break
#     if i>150:
#         continue
#     if i%5==0:
#         print(i)
#

def display(*numbers):
    numbers_list=[]
    for i in numbers:
         if i>500:
            break
         if i>150:
            continue
         if i%5==0:
            numbers_list.append(i)
    return(numbers_list)

a= display(12, 75, 150, 180, 145, 525, 50)

# print(a)

for i in a:
    print(i)
