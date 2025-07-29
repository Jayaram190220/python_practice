# Exercise 16: Check Palindrome Number
given_number=1221
rev_num=0
temp_number=given_number

while temp_number>0:
    last_digit=temp_number%10
    rev_num=rev_num*10+last_digit
    temp_number=temp_number//10

# print(temp_number)
# print(rev_num)
# print(given_number)

if given_number==rev_num:
    print("Its a palindrome")
else:
    print("Not a palindrome")
