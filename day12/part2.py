import re

f = open( "input", "r").read().strip().split("\n")

# parse: initial state: #..#.#..##......###...###
matches = re.match("initial state: ([#.]+)", f[0] )
state = list(matches.group(1))

prepadding=0

def pad_state(state):
    global prepadding

    for i in range(0,3):
        if state[i] != '.':
            state.insert(i, '.')
            prepadding += 1

    for i in range(0, 3):
        if state[len(state) - 1 - i ] != '.':
            state.append('.')

    return state

# rules!
rules = list()
for i in range(2, len(f)):
    matches = re.match("([#.]{5}) => ([#.])", f[i])
    rules.append( ( matches.group(1), matches.group(2) ) )

def score(state):
    global prepadding

    sum = 0
    for i in range(0, len(state)):
        if state[i] == '#':
            sum += i - prepadding

    return sum

# generations
scores = list()
for gen in range(0, 1000):
    state = pad_state(state)
    new_state = list(state)

    #apply rules to each non-padded members
    for c in range( 2, len(state) - 2):
        matches = False

        for ( rule, result ) in rules:
            if state[c] == rule[2] and state[c-1] == rule[1] and state[c-2] == rule[0] and state[c+1] == rule[3] and state[c+2] == rule[4]:
                new_state[c] = result
                matches = True
                break

            if not matches:
                new_state[c] = '.'

    state = new_state
    scores.append( score(state) )
    # so noisy!
    # print(score(state), " ", gen, " -> ", "".join(state))

delta = ( scores[-1] - scores[-2] )
print( score(state) + delta * ( 50000000000 - ( gen + 1 ) ) )