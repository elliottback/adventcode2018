from collections import deque

f = open( "input", "r").read().strip()
numbers = deque( map( int, f.split(" ") ) )

def parseMeta(arr):
    numChildren = arr.popleft()
    numMetaDir = arr.popleft()
    sum = 0

    childrenDict = {}
    for c in range(1,numChildren + 1):
        childrenDict[c] = parseMeta( arr )

    # now the good stuff
    if numChildren == 0:
        for c in range(numMetaDir):
            sum += arr.popleft()
    else:
        for c in range(numMetaDir):
            idx = arr.popleft()
            if idx != 0 and idx in childrenDict:
                sum += childrenDict[idx]

    return sum;


print( parseMeta( numbers ) )