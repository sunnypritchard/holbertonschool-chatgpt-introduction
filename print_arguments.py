#!/usr/bin/python3
import sys

# Print all arguments passed to the script except the script name
# Fix loop start to index [1] excluding the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])