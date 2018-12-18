import copy

f = open( "input", "r").read().strip().split("\n")

# init the coordinates
area = list(map( lambda r: list(r), f ))

open_ground = '.'
trees='|'
lumberyard='#'

def countAdjacentOfType( area, x, y, thing):
    count = 0

    for xx in range( x - 1, x + 2 ):
        for yy in range( y - 1, y + 2 ):
            if xx < 0 or xx >= len(area) or yy < 0 or yy >= len(area):
                continue

            if xx == x and yy == y:
                continue

            if area[xx][yy] == thing:
                count = count + 1

    return count

def openToTrees( area, x, y):
    if area[x][y] is not open_ground:
        return False

    if countAdjacentOfType(area, x, y, trees ) >= 3:
        return True

    return False

def treesToLumberYard( area, x, y ):
    if area[x][y] is not trees:
        return False

    if countAdjacentOfType(area, x, y, lumberyard ) >= 3:
        return True

    return False

def lumberYardToOpen( area, x, y ):
    if area[x][y] is not lumberyard:
        return False

    if countAdjacentOfType(area, x, y, lumberyard ) < 1 or countAdjacentOfType(area, x, y, trees) < 1:
        return True

    return False

# one step!
for i in range(0,10):
    new_area = copy.deepcopy( area )

    for x in range(0, len(area) ):
        for y in range(0, len(area[0])):
            if area[x][y] is open_ground and openToTrees(area, x, y ):
                new_area[x][y] = trees
            elif area[x][y] is trees and treesToLumberYard(area, x, y):
                new_area[x][y] = lumberyard
            elif area[x][y] is lumberyard and lumberYardToOpen(area, x, y):
                new_area[x][y] = open_ground
            else:
                new_area[x][y] = area[x][y]

    area = new_area

for x in range(0, len(area) ):
    print( "".join( area[x] ) )

print( len( [item for sublist in area for item in sublist if item == trees] ) * len( [item for sublist in area for item in sublist if item == lumberyard] ) )