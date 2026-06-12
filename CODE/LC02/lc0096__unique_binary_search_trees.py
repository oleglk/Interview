# lc0096__unique_binary_search_trees.py
# Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0096__unique_binary_search_trees import *

# RELOAD:
# import importlib; import lc0096__unique_binary_search_trees; importlib.reload(lc0096__unique_binary_search_trees); from lc0096__unique_binary_search_trees import *

# The idea: numBSTs(numNodes) = numLeftBSTs * numRightBSTs; build numBSTs from bottom up while considering all root positions.
# See https://algo.monster/liteproblems/96

def unique_binary_search_trees(n: int) -> int:
    # dp[i] will hold num of BSTs for i nodes (1..i)
    # dp[0]=1 since there is one empty subtree
    dp = [1] + [0]*n

    for numNodes in range(1, n+1):
        # try all choices of root node
        for rootPos in range(1, numNodes+1):
            # each left subtree has (rootPos - 1) nodes
            numLeftSubtrees = dp[rootPos - 1]
            # each right subtree has (numNodes - rootPos) nodes
            numRightSubtrees = dp[numNodes - rootPos]
            # take num of combo-s of all left subtrees with all right subtrees
            dp[numNodes] += numLeftSubtrees * numRightSubtrees

    return dp[n]
##


def test__unique_binary_search_trees():
    tasks = [
        0,  # 1
        1,  # 1
        2,  # 2
        3,  # 5
    ]
    for n in tasks:
        print("========================================")
        print(f"Input: n={n}")
        res = unique_binary_search_trees(n)
        print(f"Result: {res}")
##
