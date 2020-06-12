#!/usr/bin/python

import sys

print ("Command Line Arguments are:", str(sys.argv))

if (len(sys.argv)==4):
    if ( sys.argv[1] >= sys.argv[2]) and (sys.argv[1] >= sys.argv[3]):
        print(sys.argv[1], "is the biggest number")
    elif (sys.argv[2] >= sys.argv[1]) and (sys.argv[2] >= sys.argv[3]):
        print(sys.argv[2],"is the biggest number")
    else:
        print(sys.argv[3], "is the biggest number")
else:
    print("Please provide 3 numbers only to find biggest number")
    