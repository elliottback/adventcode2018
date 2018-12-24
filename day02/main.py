import re
from collections import Counter

def checksum( val, len ):
    for count in Counter(val).values():
        if( count == len):
            return True
    return False

f = open( "input", "r")

contents = f.read()

lines = contents.split("\n")

threes = twos = 0;

for line in lines:
    if checksum(line, 2):
        twos += 1

    if checksum(line, 3):
        threes += 1

print( threes * twos )