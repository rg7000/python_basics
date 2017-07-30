import os
import sys

try:
    file_name = "task_file.txt"
    if(os.path.isfile(file_name)):
        if len(sys.argv) > 1:
            if sys.argv[1] == '-v':
                f = open(file_name, "r")
                print(f.read()) 
            elif sys.argv[1] == '-a':
                f = open(file_name, "a")
                f.write(sys.argv[2]+"\n")
        else:
            print("Not enough parameters")
    else: 
        print("File not found")
except Exception as e:
    print(e)
