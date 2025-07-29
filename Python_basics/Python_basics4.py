# Exercise 4: Remove first n characters from a string

given_String="pynative"

print(given_String[4:])
print(given_String[2:])

n=int(input("enter a  number"))
for i in given_String:
    print(given_String[n:])
