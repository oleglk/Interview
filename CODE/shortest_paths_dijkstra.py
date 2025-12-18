# shortest_paths_dijkstra.py - Given weighted graph with non-negative weights and source, find shortest paths to all nodes.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from shortest_paths_dijkstra import *

# RELOAD:
# import importlib; import shortest_paths_dijkstra; importlib.reload(shortest_paths_dijkstra); from shortest_paths_dijkstra import *


## Assumptions: - graph represented by adjacency lists dictionary:
##                 nodeId -> list of (neighborId, weight)
##              - all edge weights are non-negative

# The idea: iteratively relax neighbours of the current shortest-distance-from-source node. Maintain priority queue ordered by distance-from-source.

import heapq


def shortest_paths_dijkstra(graph: list, srcId: int) -> int:
    # graph: node -> list of (neighborId, edgeWeight)
    if ( (graph is None) or (len(graph) == 0) ):
        return({})
    if ( srcId not in graph ):
        return({})
    # init distances (src to 0, others to +inf)
    dist = {node:float('inf') for node in graph}
    dist[srcId] = 0
    queue = [(0, srcId)]

    while ( queue ):
        # update ("relax") neighbours of smallest-distance node
        smallestDist, nodeId = heapq.heappop(queue)
        for neibId, edgeWeight in graph[nodeId]:
            newDist = smallestDist + edgeWeight
            if ( newDist < dist[neibId] ):
                dist[neibId] = newDist
                # update prio-queue when node distance decreases
                heapq.heappush(queue, (newDist, neibId))

    return(dist)


def test__shortest_paths_dijkstra():
    # 1
    g1 = {1:[]}
    # 1-(4)-2
    g2 = {1:[(2,4)], 2:[(1,4)]}
    # 1-(1)-2-(1)-3
    #  \         /
    #  (5)     (2)
    #     \   /
    #       4
    g3 = {1:[(2,1),(4,5)], 2:[(1,1),(3,1)], 3:[(2,1),(4,2)], 4:[(1,5),(3,2)]}
    for g in [{}, g1, g2, g3]:
        print("==========================================")
        print(f"Input: {g}")
        res = shortest_paths_dijkstra(g, 1)
        print(f"Shortest distances from {1}: {res}")
