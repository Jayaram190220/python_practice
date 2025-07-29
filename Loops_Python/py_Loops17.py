#Exercise 17: Find the sum of a series of a number up to n terms

# num=2
# terms=5
# total_sum=0
# current_term=''
#
# for i in range(1,terms+1):
#     current_term=current_term+str(num)
#     total_sum=total_sum+int(current_term)
#
# print(total_sum)

def series_number(num,terms):
    total_sum=0
    current_term=''

    for i in range(1,terms+1):
        current_term=current_term+str(num)
        total_sum=total_sum+int(current_term)
    return total_sum

a=series_number(2,5)
print(a)
