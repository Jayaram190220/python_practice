# Exercise 22: Capitalize the first letter of each word in a string
str1 = "pynative.com is for python lovers"
wrd=""
wrd_lis=[]
for i in str1:
    if i not in " ":
        wrd+=i
    if i == " ":
        wrd_lis.append(wrd)
        wrd=""
wrd_lis.append(wrd)
for i in wrd_lis:
    print(i.capitalize(),end=" ")
