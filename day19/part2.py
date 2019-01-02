# C:\Users\ellio\Downloads\pypy3-v6.0.0-win32>pypy3.exe part2.py
# arg this takes forever to run, I switched to pypy3
# it still takes forever....

import re
f = open( "input", "r").read().strip().split('\n')

# parse input
program = list()
state = [1,0,0,0,0,0]

ip_register = int( f[0].split(" ")[1] )
ip=0

for i in range(1, len(f)):
    line = re.match('([a-zA-Z]+) (\d+) (\d+) (\d+)', f[i])
    program.append( [ line.group(1), int(line.group(2)), int(line.group(3)), int(line.group(4))])

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

opMap = {
    'eqrr':eqrr,
    'eqri':eqri,
    'eqir':eqir,
    'gtrr':gtrr,
    'gtri':gtri,
    'gtir':gtir,
    'setr':setr,
    'seti':seti,
    'borr':borr,
    'bori':bori,
    'banr':banr,
    'bani':bani,
    'addr':addr,
    'addi':addi,
    'mulr':mulr,
    'muli':muli,
}

def step( state, ip_register, program ):
    global opMap;

    (op, in1, in2, out) = program[state[ip_register]]
    opMap[op](state, in1, in2, out)

i = 0
while i < 10000:
    state[ip_register] = ip
    step(state, ip_register, program)
    ip = state[ip_register] + 1
    i += 1

print( "https://www.wolframalpha.com/input/?i=sum+of+factors+of+" + str(state[1] ) )