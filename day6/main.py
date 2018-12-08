from operator import itemgetter

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
for x in range(0, maxX + 1):
    for y in range(0, maxY + 1):
        distances = {}
        for coordinate in coordinates:
            distances[ coordinate ] = manhattanDistance(coordinate[0], x, coordinate[1], y)

        sortedDistances = sorted(distances.items(), key=itemgetter(1))

        if map[x] is None:
            map[x]=[None] * ( maxY + 1 )

        if sortedDistances[0][1] == sortedDistances[1][1]:
            map[x][y] = None
        else:
            map[x][y]= sortedDistances[0][0] # the winner

# flush all coordinates who touch our edges
for infinite in set(map[0][:]) | set(map[maxX][:]) | set([sublist[0] for sublist in map]) | set([sublist[maxY] for sublist in map]):
    if infinite in coordinates:
        coordinates.remove(infinite)

coordinates = {key: None for key in coordinates} #map me
final = {}

for x in range(0, maxX + 1):
    for y in range(0, maxY + 1):
        if map[x][y] not in coordinates:
            continue
        else:
            if map[x][y] not in final:
                final[map[x][y]] = 0
            final[map[x][y]] = final[map[x][y]] + 1
final = sorted(final.items(), key=itemgetter(1) )
print( final[len(final)-1] )