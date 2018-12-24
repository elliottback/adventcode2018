import re

f = open( "input", "r").read().strip()

graph = {}
nodes = []

for line in f.split("\n"):
    matches = re.match( "Step ([A-Z]+) must be finished before step ([A-Z]+) can begin.", line )

    if matches[2] not in graph:
        graph[matches[2]] = []

    if( matches[2] not in nodes ):
        nodes.append(matches[2])

    if (matches[1] not in nodes):
        nodes.append(matches[1])

    graph[matches[2]].append( matches[1] )

nodes.sort()

def findNodeWithNoDeps(nodes, graph):
    for node in nodes:
        if node not in graph:
            return node
        elif len(graph[node]) == 0:
            return node
    return None

result=""
while len(nodes) > 0:
    satisfied = findNodeWithNoDeps(nodes, graph)
    result += satisfied

    # take this one off deps
    for node in graph:
        if satisfied in graph[node]:
            graph[node].remove(satisfied)

    #take off nodes
    nodes.remove(satisfied)

print(result)