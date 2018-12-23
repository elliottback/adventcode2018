import re
from collections import deque

f = open( "input", "r").read().strip().split("\n")

# parse: initial state: #..#.#..##......###...###
matches = re.match("initial state: ([#.]+)", f[0] )
state = list(matches.group(1))

def pad_state(state):
    for i in range(0,3):
        state.insert(0, '.')

    for i in range(0, 3):
        state.append('.')
    return state

# rules!
rules = list()
for i in range(2, len(f)):
    matches = re.match("([#.]{5}) => ([#.])", f[i])
    rules.append( ( matches.group(1), matches.group(2) ) )

# generations
for gen in range(0, 20):
    state = pad_state(state)
    new_state = list(state)

    #apply rules to each non-padded members
    for c in range( 2, len(state) - 2):
        for ( rule, result ) in rules:
            if state[c] == rule[2] and state[c-1] == rule[1] and state[c-2] == rule[0] and state[c+1] == rule[3] and state[c+2] == rule[4]:
                new_state[c] = result
                break
            else:
                new_state[c] = '.'

    state = new_state
    print(gen, " -> ", "".join(state))

initial_pot_position = 3 * ( gen + 1 )

sum = 0
for i in range(0, len(state)):
    if state[i] == '#' :
        sum += i - initial_pot_position

print(sum)