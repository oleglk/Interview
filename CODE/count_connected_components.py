# count_connected_components.py - Count Connected Components in a graph using union-find.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from count_connected_components import *

# RELOAD:
# import importlib; import count_connected_components; importlib.reload(count_connected_components); from count_connected_components import *


# The idea: first build disjoined sets by merging components on edges, then count the components using a dictionary.

from collections import defaultdict

class Solution:
    def __init__(n, edges):
        self.numNodes = n
        self.parent = list(range(0, n)) # initially each node is parent of itself
        self.compDict = defaultdict(list)

    def find(x: int) -> int:
        """Finds parent of element x. Optimizes the array while searching"""
        if ( x != 
    
