# Exercise 11: Get each digit from a number in the reverse order.

given_number=7536
rev_num=0
temp_number=given_number

while temp_number>0:
    last_digit=temp_number%10
    print(last_digit,end=" ")
    temp_number=temp_number//10
