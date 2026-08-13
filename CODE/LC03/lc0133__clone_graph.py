# lc0133__clone_graph.py
# Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0133__clone_graph import *

# RELOAD:
# import importlib;    import lc0133__clone_graph;  importlib.reload(lc0133__clone_graph);  from lc0133__clone_graph import *

# The idea: maintain dictionary of {node::cloned_node}. Build cloned graph during BFS traversal of the original graph.
# See: https://www.geeksforgeeks.org/dsa/clone-an-undirected-graph/


class Node:
    def __init__(self, v: int) -> None:
        self.val = v
        self.neighbors = []

##

from collections import deque


def clone_graph(node: Node) -> Node:
    if ( node is None ):
        return None

    oldToNew = {}  # "visited" and more
    oldToNew[node] = Node(node.val)
    queue = deque([node])  # the queue will hold original-graph nodes
                           # that already have clones

    while ( queue ):
        currNode = queue.popleft()  # clone of 'currNode' should already exist

        for neighbor in currNode.neighbors:
            if ( neighbor not in oldToNew ):
                # create new clone and schedule for processing
                oldToNew[neighbor] = Node(neighbor.val)
                queue.append(neighbor)
            # connect cloned nodes
            oldToNew[currNode].neighbors.append(oldToNew[neighbor])

    return oldToNew[node]
##


# Compare two graphs structurally and by values
# (copied as-is from https://www.geeksforgeeks.org/dsa/clone-an-undirected-graph/)
def compareGraphs(n1, n2, visited):
    
    if not n1 or not n2:
        return n1 == n2
        
    if n1.val != n2.val or n1 is n2:
        return False

    visited[n1] = n2

    if len(n1.neighbors) != len(n2.neighbors):
        return False

    for i in range(len(n1.neighbors)):
        neighbor1 = n1.neighbors[i]
        neighbor2 = n2.neighbors[i]

        if neighbor1 in visited:
            if visited[neighbor1] != neighbor2:
                return False
                
        else:
            if not compareGraphs(neighbor1, neighbor2, visited):
                return False

    return True
##


def test__clone_graph():
    #  1 - 2
    #  |   |
    #  3 - 4
    g1n1 = Node(1);  g1n2 = Node(2);  g1n3 = Node(3);  g1n4 = Node(4)
    g1n1.neighbors = [g1n2, g1n3]
    g1n2.neighbors = [g1n1, g1n4]
    g1n3.neighbors = [g1n1, g1n4]
    g1n4.neighbors = [g1n2, g1n3]
    #    1
    #   / \
    #  2   3
    g2n1 = Node(1);  g2n2 = Node(2);  g2n3 = Node(3)
    g2n1.neighbors = [g2n2, g2n3]
    g2n2.neighbors = [g2n1]
    g2n3.neighbors = [g2n1]

    tasks = [g1n1, g2n1]
    for node in tasks:
        print("==================================================")
        newNode = clone_graph(node)
        isEqual = compareGraphs(node, newNode, {})
        print(f"IsEqual = {isEqual}")
##
