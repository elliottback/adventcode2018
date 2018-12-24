import copy

f = open( "input", "r").read().strip().split("\n")

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
        temp[x][y] = v

    for y in range(0, len(temp)):
        print("".join(temp[y]))

def checkCollisions():
    global carts

    collisions = {}

    for (x,y, _, _2 ) in carts:
        if (x,y) not in collisions:
            collisions[ (x,y) ] = 1
        else:
            collisions[(x, y)] = collisions[(x, y)] + 1

    return {k: v for k, v in collisions.items() if v > 1 }

# iterate until we crash!!!!
printTracks()
while True:
    collisions = checkCollisions()

    if len(collisions) > 0:
        crash = collisions.popitem()
        print( crash[0][1], ",", crash[0][0])
        break

    for index, (x, y, velocity, _) in enumerate(carts):
        # 1: make ur move
        # going up
        if velocity == '^':
            if tracks[x-1][y] == '/':
                carts[index][2] = '>'
                carts[index][0] -= 1
            elif tracks[x-1][y] == '\\':
                carts[index][2] = '<'
                carts[index][0] -= 1
            elif tracks[x-1][y] == '|' or tracks[x-1][y] == '+':
                carts[index][0] -= 1
            else:
                raise ValueError("going up with an issue boss!")
        # going down
        elif velocity == 'v':
            if tracks[x+1][y] == '/':
                carts[index][2] = '<'
                carts[index][0] += 1
            elif tracks[x+1][y] == '\\':
                carts[index][2] = '>'
                carts[index][0] += 1
            elif tracks[x+1][y] == '|' or tracks[x+1][y] == '+':
                carts[index][0] += 1
            else:
                raise ValueError("going down with an issue boss!")
        # going right
        elif velocity == '>':
            if tracks[x][y+1] == '/':
                carts[index][2] = '^'
                carts[index][1] += 1
            elif tracks[x][y+1] == '\\':
                carts[index][2] = 'v'
                carts[index][1] += 1
            elif tracks[x][y+1] == '-' or tracks[x][y+1] == '+':
                carts[index][1] += 1
            else:
                raise ValueError("going down with an issue boss!")
        # going left
        elif velocity == '<':
            if tracks[x][y-1] == '/':
                carts[index][2] = 'v'
                carts[index][1] -= 1
            elif tracks[x][y-1] == '\\':
                carts[index][2] = '^'
                carts[index][1] -= 1
            elif tracks[x][y-1] == '-' or tracks[x][y-1] == '+':
                carts[index][1] -= 1
            else:
                raise ValueError("going down with an issue boss!")

        # 2: if you landed on an intersection, change direction
        (x,y) = ( carts[index][0],  carts[index][1] )
        if tracks[x][y] == '+':
            carts[index][2] = next_direction( carts[index][2], carts[index][3] )
            carts[index][3] = ( carts[index][3] + 1 ) % 3