f = open( "input", "r").read().strip()
number = int(f)

# init the coordinates
recipes = [3,7]
(elf1, elf2) = (0, 1)

while len(recipes) <= number + 10:
    score = recipes[elf1] + recipes[elf2]

    if score < 10:
        recipes.append(score)
    else:
        for digit in str(score):
            recipes.append(int(digit))

    elf1 = ( elf1 + recipes[elf1] + 1 ) % len(recipes)
    elf2 = ( elf2 + recipes[elf2] + 1 ) % len(recipes)

print( "".join( map(str, recipes[ number : number + 10 ] ) ) )