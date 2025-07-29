#Exercise 2: Print the Sum of a Current Number and a Previous number

for i in range(1,11):
    prev_num=i-1
    if prev_num<0:
        prev_num=0
    total_sum=i+prev_num
    print(f"Current Number {i} Previous Number {prev_num}  Sum:  {total_sum}")
