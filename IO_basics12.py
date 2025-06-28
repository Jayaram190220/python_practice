#Exercise 12: Interactive Menu

print(" please select any option in 1, 2, 3")
option1=int(input("enter option:"))
while True:
    if option1 not in [1,2,3]:
        print("invalid option")
    if option1==1:
        print("say hello")
    elif option1==2:
        num=int(input("enter number:"))
        print(num*num)
    elif option1==3:
        print("exit")
    break
