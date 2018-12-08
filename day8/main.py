from collections import deque

f = open( "input", "r").read().strip()
numbers = deque( map( int, f.split(" ") ) )

def parseMeta(arr):
    numChildren = arr.popleft()
    numMetaDir = arr.popleft()
    sum = 0;

    for c in range(numChildren):
        sum += parseMeta( arr )

    # now the good stuff
    for c in range(numMetaDir):
        sum += arr.popleft()

    return sum;


print( parseMeta( numbers ) )