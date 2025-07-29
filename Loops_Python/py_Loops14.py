#Exercise 14: Reverse a integer number

# num=76542
# rev_num=0
# while num>0:
#     lastdigit=num%10
#     rev_num=rev_num*10+lastdigit
#     num=num//10
# print(rev_num)

def rev_number(num):
    rev_num=0
    while num>0:
        lastdigit=num%10
        rev_num=rev_num*10+lastdigit
        num=num//10
    return rev_num

a=rev_number(76542)
print(a)
