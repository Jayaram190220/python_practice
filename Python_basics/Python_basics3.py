#Exercise 3: Print characters present at an even index number

org_string="PYnative"
#By using counter
cntr=0
for i in org_string:
    if cntr%2==0:
        print(i)
    cntr=cntr+1
print()
#By using range
for i in range(len(org_string)):
    if i%2==0:
        print(org_string[i])
