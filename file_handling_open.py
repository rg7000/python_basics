file_name = "my_tasks.txt"
f = open(file_name, "w")
f.write("1. Hi\n")
f.write("2. hello\n")
f.close()

f = open(file_name,"a")
f.seek(1)
f.write("3. Appending the file\n")
f.close()

#f = open(file_name, "r")
#print(f.seek(4))
print("Done")
