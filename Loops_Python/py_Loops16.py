#Exercise 16: Calculate the cube of all numbers from 1 to a given number

input_number = 6

for i in range(1,input_number+1):
    print(f'Current Number is : {i}  and the cube is {i*i*i}')

def cube_number(num):
    cube_string=""
    for i in range(1,num+1):
        cube_string=cube_string+int(i)
    return cube_string

a=cube_number(6)
print(a)
