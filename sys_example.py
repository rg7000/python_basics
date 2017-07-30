import sys
import os

if len(sys.argv) == 1:
    print("Error")
    sys.exit(1)
if len(sys.argv) >= 1:
    file_name = sys.argv[1]
    if not os.path.isfile(file_name):
        with open(file_name, "w") as f:
             f.write("Written file")
