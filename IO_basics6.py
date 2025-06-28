#Exercise 6: Write all content of a file into a new file by skipping line number 5

with open("sample.txt","r") as file1:
    with open("new_file.txt","w") as file2:
        content_file=file1.readlines()
        for i in content_file:
            if i!="line5\n":
                file2.write(i)
