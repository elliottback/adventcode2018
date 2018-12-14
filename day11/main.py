f = open( "input", "r").read().strip()
serial = int(f)

[ minX, maxX, minY, maxY ] = [1, 300, 1, 300]

def rackId( x_coordinate):
    return x_coordinate + 10

def powerLevel( x_coordinate, y_coordinate, serial ):
    power = rackId( x_coordinate ) * ( rackId( x_coordinate ) * y_coordinate + serial )
    hundreds = int((int(power) / int(100))) % 10
    return hundreds - 5

def gridPower( x, y, serial, maxX, maxY ):
    if x + 3 > maxX or y + 3 > maxY:
        return 0

    sum = 0;
    for xx in range(x, x + 3):
        for yy in range( y, y + 3):
            sum += powerLevel(xx, yy, serial)
    return sum

max = 0
max_coordinates=None

for x in range(minX, maxX+1):
    for y in range(minY, maxY + 1):
        power = gridPower(x, y, serial, maxX, maxY)
        if power > max:
            max = power
            max_coordinates = [x,y]

print( max, max_coordinates )