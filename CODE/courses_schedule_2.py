# courses_schedule_2.py - Given numCourses and prerequisites pairs, return ordering of all courses or empty list if impossible.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from courses_schedule_2 import *

# RELOAD:
# import importlib; import courses_schedule_2; importlib.reload(courses_schedule_2); from courses_schedule_2 import *


from collections import defaultdict, deque

def courses_schedule_2(numCourses: int, prerequisitePairs: list) -> list:
    adjacency = defaultdict(list)  # dependency graph as adjacency list
    inDegree = [0]*numCourses
    for a,b in prerequisitePairs:  # b depends on a
        adjacency[a].append(b)
        inDegree[b] += 1
    # init the queue with courses without dependencies
    queue = deque([c for c in range(0, numCourses) if (inDegree[c] == 0)])

    order = []  # the resulting order
    while ( queue ):
        u = queue.popleft()  # u is a course with no unresolved dependencies
        order.append(u)
        for v in adjacency[u]:  # update cources that are dependent on u
            inDegree[v] -= 1
            if ( inDegree[v] == 0 ):
                queue.append(v)  # all dependencies of v became resolved

    return order if (len(order) == numCourses) else []


def test__courses_schedule_2():
    # 0-1-2
    g1 = [3, [[0,1], [1,2]]]  # 0,1,2
    # 0-1-2-3 4-5
    #   ^-^-----+
    g2 = [6, [[0,1], [1,2], [2,3], [4,5], [5,1], [5,2]]]  # 0,4,5,1,2,3
    # 0
    g3 = [1, []]  # 0
    g4 = [2, []]  # 0,1
    # 0-1
    # ^-+
    g5 = [2, [[0,1], [1,0]]]  # []
    #     +---+
    # 0-1-2-3 4
    # ^-----+
    g6 = [5, [[0,1], [1,2], [2,3], [3,0], [2,4], [4,2]]]  # []
    
    for numCourses, edges in [g1, g2, g3, g4, g5, g6]:
        print("===========================")
        print(f"Input: numCourses={numCourses}, edges={edges}")
        res = courses_schedule_2(numCourses, edges)
        print(f"Result: {res}")
