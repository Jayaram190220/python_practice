#Exercise 10: Read Line Number 4 from File


with open("sample.txt","r") as file1:
    content_file=file1.readlines()
    for i in content_file:
        if i=="line4\n":
            print(i)
