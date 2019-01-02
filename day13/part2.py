import copy
import sys
from termcolor import colored

f = open( "input", "r").read().split("\n")

# our grid
tracks = list( map( lambda line: list(line), f ) )

def next_direction( current, idx ):
    if idx == 1:
        return current
    elif idx == 0 and current == "^":
        return "<"
    elif idx == 0 and current == "v":
        return ">"
    elif idx == 0 and current == "<":
        return "v"
    elif idx == 0 and current == ">":
        return "^"
    elif idx == 2 and current == ">":
        return "v"
    elif idx == 2 and current == "v":
        return "<"
    elif idx == 2 and current == "^":
        return ">"
    elif idx == 2 and current == "<":
        return "^"
    else:
        raise ValueError("where do I turn!")

# find the carts
carts=list()
for x in range(0, len(tracks)):
    for y in range(0, len(tracks[x])):
        if tracks[x][y] == "<" or tracks[x][y] == ">" or tracks[x][y] == "^" or tracks[x][y] == "v":
            carts.append( [ x, y, tracks[x][y], 0 ] )

            if tracks[x][y] == "<" or tracks[x][y] == ">":
                tracks[x][y] = "-"
            else:
                tracks[x][y] = "|"

# printer
def printTracks():
    global carts
    global tracks

    temp = copy.deepcopy( tracks )

    for (x, y, v, _) in carts:
        temp[x][y] = colored(v, 'red')

    for y in range(0, len(temp)):
        print("".join(temp[y]))
    print("\n")

def checkCollisions():
    global carts

    collisions = {}

    for cart in carts:
        tuple = (cart[0], cart[1])
        if tuple not in collisions:
            collisions[ tuple ] = [ cart ]
        else:
            collisions[ tuple ].append( cart )

    return collisions

# iterate until we crash!!!!
printTracks()
while True:
    # sort carts
    carts.sort( key = lambda i: ( i[0], i[1] ) )

    if len(carts) <= 1:
        print( carts[0][1], ",", carts[0][0] )
        break

    carts_that_we_nuke = list()

    for index, (x, y, velocity, _) in enumerate(carts):
        # 1: make ur move
        # going up
        if velocity == '^':
            carts[index][0] -= 1
            if tracks[x-1][y] == '/':
                carts[index][2] = '>'
            elif tracks[x-1][y] == '\\':
                carts[index][2] = '<'
        # going down
        elif velocity == 'v':
            carts[index][0] += 1
            if tracks[x+1][y] == '/':
                carts[index][2] = '<'
            elif tracks[x+1][y] == '\\':
                carts[index][2] = '>'
        # going right
        elif velocity == '>':
            carts[index][1] += 1
            if tracks[x][y+1] == '/':
                carts[index][2] = '^'
            elif tracks[x][y+1] == '\\':
                carts[index][2] = 'v'
        # going left
        elif velocity == '<':
            carts[index][1] -= 1
            if tracks[x][y-1] == '/':
                carts[index][2] = 'v'
            elif tracks[x][y-1] == '\\':
                carts[index][2] = '^'
        # 2: if you landed on an intersection, change direction
        (x,y) = ( carts[index][0],  carts[index][1] )
        if tracks[x][y] == '+':
            carts[index][2] = next_direction( carts[index][2], carts[index][3] )
            carts[index][3] = ( carts[index][3] + 1 ) % 3

        # 3: check and remove collisions
        collisions = checkCollisions()
        for k, cartslist in collisions.items():
            if len(cartslist) > 1:
                print("collision: ", k)
                for cart in cartslist:
                    carts_that_we_nuke.append(cart)

    for cart in carts_that_we_nuke:
        if cart in carts:
            carts.remove(cart)