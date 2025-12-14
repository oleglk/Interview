# courses_schedule.py - Given numCourses and prerequisites pairs, determine if you can finish all courses.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from courses_schedule import *

# RELOAD:
# import importlib; import courses_schedule; importlib.reload(courses_schedule); from courses_schedule import *


# The idea: Kahn's algorithm fot topological sort will be unable to pick any node belonging to a cycle as the one with zero in-degree (they all have incoming edges). Thus the whole cycle will not appear in the resulting sorted list.
#  Kahn's algorithm idea - start with nodes of in-degree=0, append to result, "remove" their outgoing edges, loop...


# Datastructures involved
# - Graph represented by adjacency list - dictionary of outgoing edge lists
# --      (items are {vertex :: list-of-neighbours})
# - In-degrees held in {vertex :: in-degree} dictionary
# - 0-degrees vertices move through a FIFO queue
# - Result is an ordered lists

from collections import deque


def courses_schedule(numCourses: int, prerequisitePairs: list) -> list:
    # make input for topological sort (adjLists dictionary {vert :: [targets]})
    adjLists = {}
    for v in range(0, numCourses):
        adjLists[v] = []
    for source, target in prerequisitePairs:
        adjLists[source].append(target)

    # run topological sort and check whether all nodes are processed
    sortedList = topological_sort(adjLists)
    return(len(sortedList) == numCourses)
    


def _calc_indegrees(adjLists: dict) -> dict:
    vertexToInDegree = {}
    for vertex in adjLists.keys():
        vertexToInDegree[vertex] = 0  # init all in-degrees to 0
    for targets in adjLists.values():
        for edgeTarget in targets:
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
        # update neighbours of 'zeroInVertex'
        for target in adjLists[zeroInVertex]:
            vertexToInDegree[target] -= 1
            if ( vertexToInDegree[target] == 0 ):  # 'target' becomes 0-in
                queue.append(target)
    return(sortedList)


def test__courses_schedule():
    # 0-1-2
    g1 = [3, [[0,1], [1,2]]]  # Result: True
    g2 = [6, [[0,1], [1,2], [2,3], [4,5], [5,1], [5,2]]]  # Result: True
    g3 = [1, []]  # Result: True
    g4 = [2, []]  # Result: True
    g5 = [2, [[0,1], [1,0]]]  # Result: False
    g6 = [5, [[0,1], [1,2], [2,3], [3,0], [2,4], [4,2]]]  # Result: False
    
    for numCourses, edges in [g1, g2, g3, g4, g5, g6]:
        print("===========================")
        print(f"Input: numCourses={numCourses}, edges={edges}")
        res = courses_schedule(numCourses, edges)
        print(f"Result: {res}")
