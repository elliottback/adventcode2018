import time

# runs in a few minutes in pypy, so OK...

f = open( "input", "r").read().strip()
serial = int(f)

[ minX, maxX, minY, maxY ] = [1, 300, 1, 300]

def rackId( x_coordinate):
    return x_coordinate + 10

def powerLevel( x_coordinate, y_coordinate, serial ):
    power = rackId( x_coordinate ) * ( rackId( x_coordinate ) * y_coordinate + serial )
    hundreds = int((int(power) / int(100))) % 10
    return hundreds - 5

# this would be so much better if you realized all squares of size (n+1) are the
# previous result plus the sum of their neighbors

#unroll 1 loop:
cache=[[0 for i in range(maxX+1)] for j in range(maxY+1)]

for x in range(minX, maxX+1):
    for y in range(minY, maxY + 1):
        cache[x][y] = powerLevel(x, y, serial,)

def gridPower( x, y, maxX, maxY, size ):
    if x + size > maxX or y + size > maxY:
        return 0

    sum = 0;
    for xx in range(x, x + size):
        for yy in range( y, y + size):
            sum += cache[xx][yy]
    return sum

max = 0
max_coordinates=None
max_size=0

def progress( total ):
    current = 0
    startTime = time.time()

    def worker():
        nonlocal current
        nonlocal startTime

        current += 1
        print("%d/%d (%d%%) %d seconds left" % ( current, total, current/total * 100, ( time.time() - startTime ) * total / current ))

    return worker

p = progress(300)
for ss in range(1, 301):
    for x in range(minX, maxX+1-ss+1):
        for y in range(minY, maxY + 1-ss+1):
            power = gridPower(x, y, maxX, maxY, ss )
            if power > max:
                max = power
                max_coordinates = [x,y]
                max_size=ss
    p()

print( max, max_coordinates, max_size )