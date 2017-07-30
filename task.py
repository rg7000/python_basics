import sys
import os

file_name = "task_file.txt"

if len(sys.argv) == 1:
    print("Insufficient arguments")
elif len(sys.argv) == 2:
    arg1 = sys.argv[1]
    if arg1 == '-v':
        f = open(file_name, "r")
        print(f.read())    
        f.close()
elif len(sys.argv) == 3:
    arg1 = sys.argv[1]
    if arg1 == '-a':
         f = open(file_name, "a")
         f.write(sys.argv[2]+"\n")
         f.close()

#use try except
