import re
from collections import Counter

class Claim:
    def __init__(self, line):
        matches = re.match( r"#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)", line )
        self.id = int(matches.group(1))
        self.left_inches = int(matches.group(2))
        self.top_inches = int(matches.group(3))
        self.width = int(matches.group(4))
        self.height = int(matches.group(5))

    def coordinates(self):
        positions = list()
        for x in range( self.left_inches, self.left_inches + self.width ):
            for y in range( self.top_inches, self.top_inches + self.height):
                positions.append((x,y))
        return positions

f = open( "input", "r")

contents = f.read()
lines = contents.split("\n")
squares = {}

for line in lines:
    claim = Claim(line)
    for coordinate in claim.coordinates():
        if coordinate not in squares:
            squares[coordinate] = 1
        else:
            squares[coordinate ] = squares[coordinate ] + 1

filtered = {k:v for k,v in squares.items() if v > 1};

print( len(filtered))

exit(0)