# strongly_connected_components.py - Find SCCs in directed graph using finish order and transpose.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from strongly_connected_components import *

# RELOAD:
# import importlib; import strongly_connected_components; importlib.reload(strongly_connected_components); from strongly_connected_components import *


## Assumption: - graph represented by two lists - of nodes and of edges
##             - edge is (u, v)

# The idea - Kosaraju algorithm:
# 1. call DFS1 on G to compute finishing times u:f for each vertex u - build a list representing finishing order
# 2. compute G-Transpose
# 3. call DFS2 on G-Transpose, but in the main loop of DFS, consider the vertices in order of decreasing u:f (as computed in line 1- take from reversed order-list)
# 4. output the vertices of each tree in the depth-first forest formed in line 3 as a separate strongly connected component


from collections import defaultdict


# DFS1 builds the ordered list of finishing times for graph vertices
def dfs1(nodeU, adjDict, visitedSet, finishOrderList):
    visitedSet.add(nodeU)
    for nodeV in adjDict[nodeU]:
        if ( nodeV not in visitedSet ):
            dfs1(nodeV, adjDict, visitedSet, finishOrderList)
    finishOrderList.append(nodeU)
    return


# Each top-level call of DFS2 traverses one SCC
def dfs2(nodeU, adjDictT, visitedSet, currSCC):
    #print(f"dfs2({nodeU}, visited:{visitedSet})")
    visitedSet.add(nodeU)
    currSCC.append(nodeU)
    for nodeV in adjDictT[nodeU]:
        if ( nodeV not in visitedSet ):
            dfs2(nodeV, adjDictT, visitedSet, currSCC)
    return


def strongly_connected_components(graphNodes, graphEdges):
    # build direct- and inverted adjacency list dictionaries for the two DFS-s
    adjDictDirect = defaultdict(list);  adjDictTransp = defaultdict(list)
    for u,v in graphEdges:
        adjDictDirect[u].append(v)  # defaultdict was initialized to empty list
        adjDictTransp[v].append(u)  # defaultdict was initialized to empty list

    # Find node-finishing order using DFS1
    visitedSet = set()
    finishOrderList = []
    for node in graphNodes:
        if ( node not in visitedSet ):
            dfs1(node, adjDictDirect, visitedSet, finishOrderList)
    #print(f"DFS-finish-order: {finishOrderList}")

    # Find all SCC-s using DFS2
    visitedSet = set()
    allSCCs = []
    for node in reversed(finishOrderList):
        if ( node not in visitedSet ):
            currSCC = []
            dfs2(node, adjDictTransp, visitedSet, currSCC)
            allSCCs.append(currSCC)

    return(allSCCs)
    

def test__strongly_connected_components():
    # 1
    g1 = [ [],  [1] ]
    # 1>--->2
    g2 = [ [(1,2)], [1,2] ]
    # 1>--->2>--->3
    #  >         <
    #  ---     ---
    #     >   <
    #       4
    g3 = [ [(1,2),(2,3),(3,4),(1,4)],  [1,2,3,4] ] 
    # 1>--->2>---->3
    #       /\    \/
    #       --    --
    #       /\    \/
    #       4<----<5
    g4 = [ [(1,2),(2,3),(3,5),(5,4),(4,2)],  [1,2,3,4,5] ]
    # 1>--->2>---->3>--->6>---->7
    #       /\    \/     /\    \/
    #       --    --     --    --
    #       /\    \/     /\    \/
    #       4<----<5     8<----<9
    g5 = [ [(1,2),(2,3),(3,5),(5,4),(4,2),
            (3,6),(6,7),(7,9),(9,8),(8,6)],  [1,2,3,4,5] ]

    for edges, nodes  in  [g1, g2, g3, g4, g5]:
        print("==================================================")
        print(f"Edges: {edges},  vertices: {nodes}")
        allSCCs = strongly_connected_components(nodes, edges)
        print(f"Result: {allSCCs}")
