f = open("input", "r").read().strip();
lines = f.split("\n");

def manhattanDistance( x1, x2, y1, y2):
    return abs(x2 - x1) + abs( y2 - y1)

coordinates = list( map( lambda x : tuple( map(int, x.split(",") ) ), lines ) )

maxX = max( list( map( lambda x: x[0], coordinates ) ) )
maxY = max( list( map( lambda x: x[1], coordinates ) ) )

map = [None] * ( maxX + 1 )

# let's just calculate the distance for every point in this grid
# and toss the ties as a None
region=0
for x in range(0, maxX + 1):
    for y in range(0, maxY + 1):

        distance = 0
        for coordinate in coordinates:
            distance += manhattanDistance(coordinate[0], x, coordinate[1], y)

        if distance < 10000:
            region = region + 1

print(region)