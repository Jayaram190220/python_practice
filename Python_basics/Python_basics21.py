# Exercise 21: Check if a user-entered string contains any digits using a for loop
GIVEN_STRING="PynativePython12345"


for i in GIVEN_STRING:
    if i.isdigit():
        print(("HAS NUMBER"))
        break
else:
    print("NO string")
