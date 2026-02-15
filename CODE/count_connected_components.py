# count_connected_components.py - Count Connected Components in a graph using union-find.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from count_connected_components import *

# RELOAD:
# import importlib; import count_connected_components; importlib.reload(count_connected_components); from count_connected_components import *


# The idea: first build disjoined sets by merging components on edges, then count the components using a dictionary.

from collections import defaultdict

class Solution:
    def __init__(self, n: int, edges: list):
        self.numNodes = n
        self.parent = list(range(0, n)) # initially each node is parent of itself
        self.edges = edges
        # build the actual components
        for u, v  in self.edges:
            self.merge(u, v)
            
        
    def find_parent(self, x: int) -> int:
        """Finds parent of element x.
           Optimizes the array by path compression while searching"""
        if ( x != self.parent[x] ):
            self.parent[x] = self.find_parent(self.parent[x])
        return self.parent[x]


    def merge(self, x: int, y: int):
        """Makes root of y son of root of x"""
        parX = self.find_parent(x)
        parY = self.find_parent(y)
        if ( parX != parY ):
            self.parent[parY] = parX


    def count(self) -> int:
        compDict = defaultdict(list)  # for {parent :: list-of-nodes}
        for node, par  in enumerate(self.parent):
            #compDict[par].append(node)  # assuming all paths compressed
            compDict[self.find_parent(par)].append(node)
        return len(compDict.keys())
        

    @staticmethod
    def count_components(n: int, edges: list[int]) -> int:
        sln = Solution(n, edges)
        return sln.count()
    #########################################


def test__count_components():
    tasks = [
        [2, [(0,1)]],               # 1
        [1, []],                    # 1
        [4, [(0,1), (2,3)]],        # 2
        [5, [(1,0), (2,3), (3,4)]]  # 2
    ]
    for n, edges  in tasks:
        print("=======================================")
        print(f"Input: n={n}, edges={edges}")
        res = Solution.count_components(n, edges)
        print(f"Result: {res}")

