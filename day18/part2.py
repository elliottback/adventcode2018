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
def iter():
    global area
    new_area = copy.deepcopy( area )

    score_trees = 0
    score_lumberyard = 0

    for x in range(0, len(area) ):
        for y in range(0, len(area[0])):
            if area[x][y] is open_ground and openToTrees(area, x, y ):
                new_area[x][y] = trees
                score_trees = score_trees + 1
            elif area[x][y] is trees and treesToLumberYard(area, x, y):
                new_area[x][y] = lumberyard
                score_lumberyard = score_lumberyard + 1
            elif area[x][y] is lumberyard and lumberYardToOpen(area, x, y):
                new_area[x][y] = open_ground
            else:
                new_area[x][y] = area[x][y]
                if new_area[x][y] == trees:
                    score_trees = score_trees + 1
                elif new_area[x][y] == lumberyard:
                    score_lumberyard = score_lumberyard + 1

    area = new_area
    return score_lumberyard * score_trees

# find the repeat
S = [iter() for n in range(1,2000)]
V = [i for i,val in enumerate(S) if val == 193572]
period = V[1] - V[0]
target = ( 1000000000 - V[0] - 1) % period
print(S[V[1] + target])