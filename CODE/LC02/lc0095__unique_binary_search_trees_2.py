# lc0095__unique_binary_search_trees_2.py
# Given an integer n, return all the structurally unique BST's (binary search trees), which have exactly n nodes of unique values from 1 to n. Return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0095__unique_binary_search_trees_2 import *

# RELOAD:
# import importlib; import lc0095__unique_binary_search_trees_2; importlib.reload(lc0095__unique_binary_search_trees_2); from lc0095__unique_binary_search_trees_2 import *


# The idea: recursion. Take each number in [1..n] for root. When root=v, all possible BSTs using [1..v-1] are left subtree options, and all possible BSTs using [v+1..n] are right subtree options.

# See https://algo.monster/liteproblems/95


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left   # TreeNode
        self.right = right # TreeNode
####


def make_bsts_for_range(i: int, j: int) -> list[TreeNode]:
    # base case - empty range
    if ( i > j ):
        return [None]

    # recursive cases - use all numbers in the range for root
    result = []
    for rootVal in range(i, j+1):
        leftSubtrees = make_bsts_for_range(i, rootVal-1)
        rightSubtrees = make_bsts_for_range(rootVal+1, j)

        # assemble all tree options
        for lt in leftSubtrees:
            for rt in rightSubtrees:
                result.append(TreeNode(rootVal, lt, rt))
    return result
##


# used for "visualization"
def print_preorder(node):
    if node is None:
        print("null", end=' ')
        return
    # Deal with the node
    print(node.val, end=' ')
    # Recur on left subtree
    print_preorder(node.left)
    # Recur on right subtree
    print_preorder(node.right)
##


def test__make_bsts_for_range():
    tasks = [1, 2, 3]
    for n in tasks:
        print("=====================================")
        print(f"Input: n={n}")
        res = make_bsts_for_range(1, n)
        print("Result:")
        for r in res:
            print_preorder(r)
            print("")
##
