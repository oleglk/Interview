# topological_sort.py - Given directed acyclic graph (DAG), return a topological ordering of nodes.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from topological_sort import *

# RELOAD:
# import importlib; import topological_sort; importlib.reload(topological_sort); from topological_sort import *


# The idea: Kahn's algorithm - start with nodes of in-degree=0, append to result, "remove" their outgoing edges, loop...


# Datastructures involved
# - Graph represented by adjacency list - dictionary of outgoing edge lists
# --      (items are {vertex :: list-of-neighbours})
# - In-degrees held in {vertex :: in-degree} dictionary
# - 0-degrees vertices move through a FIFO queue
# - Result is an ordered list

from collections import deque


def _calc_indegrees(adjLists: dict) -> dict:
    vertexToInDegree = {}
    for vertex in adjLists.keys():
        vertexToInDegree[vertex] = 0  # init all in-degrees to 0
    for targets in adjLists.values():
        # 'targets' is list of edge-target vertices
        # count how many times a vertex appears as edge-target
        for edgeTarget in targets:
            if ( edgeTarget not in vertexToInDegree ):
                # in case 'edgeTarget' doesn't appear as source/key, init it now
                vertexToInDegree[edgeTarget] = 1
            else:
                vertexToInDegree[edgeTarget] += 1
    return(vertexToInDegree)


# 'adjLists' is dict {vertex :: list-of-neighbours}
# Returns topologically sorted list of vertices
def topological_sort(adjLists: dict) -> list:
    if ( len(adjLists) == 0 ):
        return([])
    vertexToInDegree = _calc_indegrees(adjLists)
    
    # insert all initial vertices with incoming degree of 0 into the queue
    queue = deque()
    for vertex, inDegree in vertexToInDegree.items():
        if ( inDegree == 0 ):
            queue.append(vertex)

    sortedList = []  # for the result

    # the main loop - dequeue and process vertices
    while ( len(queue) > 0 ):
        zeroInVertex = queue.popleft()
        sortedList.append(zeroInVertex)
        # update neighbours of 'zeroInVertex' - reduce their incoming degrees
        for target in adjLists[zeroInVertex]:
            vertexToInDegree[target] -= 1
            if ( vertexToInDegree[target] == 0 ):  # 'target' becomes 0-in
                queue.append(target)
    return(sortedList)


def test__topological_sort():
    # 0-1-2
    g1 = {0:[1], 1:[2], 2:[]}  # Result: [0,1,2]
    g2 = {0:[1], 1:[2], 2:[3], 3:[], 4:[5], 5:[1,2]}  # Result: [0,4,5,1,2,3]
    g3 = {0:[]}
    g4 = {0:[], 1:[]}
    
    for g in [g1, g2, g3, g4]:
        print("===========================")
        print(f"Input: {g}")
        res = topological_sort(g)
        print(f"Result: {res}")
