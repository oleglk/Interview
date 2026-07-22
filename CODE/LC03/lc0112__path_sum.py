# lc0112__path_sum.py
# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0112__path_sum import *

# RELOAD:
# import importlib;    import lc0112__path_sum;  importlib.reload(lc0112__path_sum);  from lc0112__path_sum import *

# The idea: recursion while subtracting current node value from remaining sum; if remaining sum becomes zero, the path is found.

from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
####


def find_path_for_sum(root: TreeNode, remainingSum: int) -> bool:
    if ( root is None ):
        return False
    
    remainingSum -= root.data
    if ( (root.left is None) and (root.right is None) and (remainingSum == 0)):
        return True

    leftHasSum = find_path_for_sum(root.left, remainingSum)
    rightHasSum = find_path_for_sum(root.right, remainingSum)
    return (leftHasSum or rightHasSum)
##


def test__find_path_for_sum():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    ## 5 - True, 3 - False
    t1n0 = TreeNode(0)
    t1n1 = TreeNode(1);    t1n2 = TreeNode(2)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = TreeNode(3);    t1n4 = TreeNode(4);     t1n5 = TreeNode(5)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.left = t1n5
    ##     0
    ##      \
    ##       1
    ##        \
    ##         2
    ## 3 - True, 4 - False
    t2n0 = TreeNode(0)
    t2n1 = TreeNode(1);    t2n2 = TreeNode(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    ## 0 - True, 1 - False
    t3n0 = TreeNode(0)
    ##      0
    ##     /
    ##    1
    ## 1 - True, 0 - False
    t4n0 = TreeNode(0)
    t4n1 = TreeNode(1)
    t4n0.left = t4n1
    ##     1
    ##    / \
    ##   0   2
    ##        \
    ##         3
    ##        /
    ##       4
    ## 10 - True, 7 - False
    t5n0 = TreeNode(1)
    t5n1 = TreeNode(0);    t5n2 = TreeNode(2);    t5n3 = TreeNode(3);    t5n4 = TreeNode(4)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3
    t5n3.left = t5n4

    tasks = [
        [t1n0, 5], # True
        [t1n0, 3], # False
        [t2n0, 3], # True
        [t2n0, 4], # False
        [t3n0, 0], # True
        [t3n0, 1], # False
        [t4n0, 1], # True
        [t4n0, 0], # False
        [t5n0, 10],# True
        [t5n0, 7], # False
    ]
    for root, sum in tasks:
        byLevels = binary_tree_level_order(root, includeNone=True)
        print(f"By levels: {byLevels}")
        print(f"Sum to find: {sum}")
        res = find_path_for_sum(root, sum)
        print(f"Has path: {res}")
##
