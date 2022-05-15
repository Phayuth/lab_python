# Get Input from command execute argument

import sys

if len(sys.argv) == 3: # see if the argument is 3
    Input1 = sys.argv[1]      # string
    Input2 = int(sys.argv[2]) # can convert to int
else:
    print("Run command : python3 file_name.py 1st_argument 2nd_argument")
    exit(1)