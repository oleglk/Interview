# shortest_paths_bellman_ford.py - Compute shortest paths with possible negative weights and detect negative cycles.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from shortest_paths_bellman_ford import *

# RELOAD:
# import importlib; import shortest_paths_bellman_ford; importlib.reload(shortest_paths_bellman_ford); from shortest_paths_bellman_ford import *


## Assumptions: - graph represented by list of edges: (nodeId1, nodeId2, weight)
##              - weights could be negative


# The idea: relax all edges length-of-max-vertices-num-path times. If all edges converged, distances are found; otherwise negative cycle exists.


def shortest_paths_bellman_ford(edges: list, vertices: list, srcId: int) -> dict:
    """edges = list of (nodeId1, nodeId2, weight)
       vertices = list of nodeId
       Returns dice of (nodeId, min-dist) or None if negative cycle found."""
    numNodes = len(vertices)
    dist = {node:float('inf') for node in vertices}
    dist[srcId] = 0
    # relax all edges 'numNodes'-1 times (length of max-vertices-num path)
    for _ in range(0, numNodes-1):
        for nodeId1, nodeId2, weight in edges:
            if ( dist[nodeId2] > dist[nodeId1] + weight ):
                dist[nodeId2] = dist[nodeId1] + weight
    # either all distances converged, or negative cycle exists
    for nodeId1, nodeId2, weight in edges:
        if ( dist[nodeId2] > dist[nodeId1] + weight ):
            return(None)
    return(dist)


def test__shortest_paths_bellman_ford():
    # 1
    g1 = [ [], [1] ]
    # 1>(4)>2
    g2 = [ [(1,2,4)], [1,2] ]
    # 1>(1)>2>(1)>3
    #  >         <
    #  (5)     (2)
    #     >   <
    #       4
    g3 = [ [(1,2,1),(2,3,1),(3,4,2),(1,4,5)], [1,2,3,4] ] 
    # 1>(3)>2>(2)>3
    #       /\    \/
    #      (-9)  (4)
    #       /\    \/
    #       4<(1)<5
    g4 = [ [(1,2,3),(2,3,2),(3,5,4),(5,4,1),(4,2,-9)], [1,2,3,4,5] ]

    for edges, vertices in [g1, g2, g3, g4]:
        print("==========================================")
        print(f"Input: {edges};    {vertices}")
        res = shortest_paths_bellman_ford(edges, vertices, 1)
        print(f"Shortest distances from {1}: {res}")


            
