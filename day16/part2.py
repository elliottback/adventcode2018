import re
f = open( "input", "r").read().strip()
f = [line for line in f.split('\n') if line.strip() != '']

# parse input
examples = list()

for i in range(0, int(len(f) / 3)):
    before = f[i * 3]
    before = re.match('Before:\s*\[(\d+), (\d+), (\d+), (\d+)\]', before)
    before = list( map(lambda n: int(n), [ before[1], before[2], before[3], before[4] ] ) )

    op = f[i * 3 + 1]
    op = re.match('(\d+) (\d+) (\d+) (\d+)', op)
    op = list(map(lambda n: int(n), [op[1], op[2], op[3], op[4]]))

    after = f[i * 3 + 2]
    after = re.match('After:\s*\[(\d+), (\d+), (\d+), (\d+)\]', after)
    after = list( map(lambda n: int(n), [ after[1], after[2], after[3], after[4] ] ) )

    examples.append( (before, op, after ) )

#define opcodes
def addr( state, in1, in2, out):
    state[out] = state[in1] + state[in2]
    return state

def addi( state, in1, in2, out):
    state[out] = state[in1] + in2
    return state

def mulr( state, in1, in2, out):
    state[out] = state[in1] * state[in2]
    return state

def muli( state, in1, in2, out):
    state[out] = state[in1] * in2
    return state

def banr( state, in1, in2, out):
    state[out] = state[in1] & state[in2]
    return state

def bani( state, in1, in2, out):
    state[out] = state[in1] & in2
    return state

def borr( state, in1, in2, out):
    state[out] = state[in1] | state[in2]
    return state

def bori( state, in1, in2, out):
    state[out] = state[in1] | in2
    return state

def setr( state, in1, in2, out):
    state[out] = state[in1]
    return state

def seti( state, in1, in2, out):
    state[out] = in1
    return state

def gtir( state, in1, in2, out):
    if in1 > state[in2]:
        state[out] = 1
    else:
        state[out] = 0
    return state


def gtri(state, in1, in2, out):
    if state[in1] > in2:
        state[out] = 1
    else:
        state[out] = 0
    return state


def gtrr(state, in1, in2, out):
    if state[in1] > state[in2]:
        state[out] = 1
    else:
        state[out] = 0

    return state

def eqir( state, in1, in2, out):
    if in1 == state[in2]:
        state[out] = 1
    else:
        state[out] = 0

    return state


def eqri(state, in1, in2, out):
    if state[in1] == in2:
        state[out] = 1
    else:
        state[out] = 0

    return state


def eqrr(state, in1, in2, out):
    if state[in1] == state[in2]:
        state[out] = 1
    else:
        state[out] = 0

    return state

allOps = [ eqrr, eqri, eqir,
           gtrr, gtri, gtir,
           setr, seti,
           borr, bori,
           banr, bani,
           addr, addi,
           mulr, muli ]

opcodemap = {}
knowncodes = set()

# map 'em
while len(opcodemap) < len(allOps):
    for example in examples:
        (before, op, after) = example

        possibleOps = set()
        for opf in allOps:
            if opf( before[:], op[1], op[2], op[3] ) == after:
                possibleOps.add(opf)

        # remove ones we already know about
        possibleOps = possibleOps - knowncodes

        if len( possibleOps ) == 1 and op[0] not in opcodemap:
            opf = possibleOps.pop()
            opcodemap[op[0]] = opf
            knowncodes.add(opf)

# simulate
state = [0,0,0,0]
f = open( "program", "r").read().strip().split("\n")
operations = list( map( lambda line: list( map( lambda n: int(n), line.split(" " ) ) ), f ) )
for (op, in1, in2, out) in operations:
    opcodemap[op](state, in1, in2, out)

print(state)