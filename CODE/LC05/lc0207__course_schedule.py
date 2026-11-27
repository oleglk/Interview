# lc0207__course_schedule.py
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0207__course_schedule import *

# RELOAD:
# import importlib;    import lc0207__course_schedule;  importlib.reload(lc0207__course_schedule);  from lc0207__course_schedule import *

# The idea: topological sort. Represent schedule as a graph (adjacency lists). Put nodes with in-degree=0 into a queue; upon extraction from queue decrement in-degree of node's neighbors and increment count of extracted nodes. In the end return True if number of nodes extracted from the queue equals number of courses.
# See: https://www.hellointerview.com/learn/code/graphs/course-schedule

from collections import deque, defaultdict

def course_schedule(numCourses: int, prerequisites: list[int]) -> bool:
    if ( numCourses <= 1 ):
        return True
    # array to keep track of in-degrees
    inDegree = [0] * numCourses
    
    # build adjacency graph and in-degree array
    graph = defaultdict(list)
    for  dst, src  in prerequisites:
        graph[src].append(dst)
        inDegree[dst] += 1
        
    # init queue of resolved courses
    queue = deque([c for c in range(0, numCourses) if (inDegree[c] == 0)])
    cntResolved = 0  # counts resolved courses - those extracted from the queue

    while queue:
        course = queue.popleft()  # take next resolved course
        cntResolved += 1
        for dst in graph[course]:  # traverse adjacency list of currrent course
            inDegree[dst] -= 1
            if ( inDegree[dst] == 0 ):  # 'dst' course becomes resolved
                queue.append(dst)

    # no more resolved courses left
    return (cntResolved == numCourses)  # True if all courses resolved
##


def test__course_schedule():
    tasks = [
        [2, [[1,0]]],                         # True
        [2, [[1,0],[0,1]]],                   # False
        [4, [[1,0],[2,1],[3,1],[2,3]]],       # True
        [5, [[1,0],[2,1],[3,2],[4,3],[1,4]]], # False
    ]
    for  numCourses, prerequisites  in tasks:
        print("===============================================")
        print(f"Input: {numCourses},  {prerequisites}")
        res = course_schedule(numCourses, prerequisites)
        print(f"Result: {res}")
##

                
