#!usr/bin/python
import os
import sys

if sys.argv[1] in ['-p', '--path']:
    path = sys.argv[2]
    name = sys.argv[3]
else:
    path = 'lessc'
    name = sys.argv[1]

os.system(path + name + ".less " + name + ".css")
