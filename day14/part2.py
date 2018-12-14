f = open( "input", "r").read().strip()
numberlist = list( map(lambda x: int(x), list(f )) )
number = int(f)

# init the coordinates
recipes = [3,7]
(elf1, elf2) = (0, 1)

counter = len( recipes )
checkerIdx = 0

# small state machine to check the next recipe
def checker( val ):
    global checkerIdx
    global counter

    if checkerIdx >= len(f):
        return True
    elif numberlist[checkerIdx] != val:
        checkerIdx = 0 #resetIt

    if numberlist[checkerIdx] == val:
        checkerIdx = checkerIdx + 1

    counter = counter + 1
    return False

while True:
    score = recipes[elf1] + recipes[elf2]

    if score < 10:
        recipes.append(score)
        if checker(score):
            break
    else:
        for digit in str(score):
            recipes.append(int(digit))
            if checker(int(digit)):
                break

    elf1 = ( elf1 + recipes[elf1] + 1 ) % len(recipes)
    elf2 = ( elf2 + recipes[elf2] + 1 ) % len(recipes)


print( counter -  len( numberlist ) )