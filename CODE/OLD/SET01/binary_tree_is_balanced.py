# binary_tree_is_balanced.py - Given a binary tree, determine if it is height-balanced (the depths of the two subtrees of every node never differ by more than 1).

# The idea: use DFS to "measure" depths. Check balance at each subtree. DFS should return the depth if balanced, -1 otherwise.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_is_balanced import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import binary_tree_is_balanced;  importlib.reload(binary_tree_is_balanced);  from binary_tree_is_balanced import *

from binary_tree_level_order_traversal import *  # for "visualization"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##



def binary_tree_is_balanced(root: Node) -> bool:
    return(dfs_height(root) != -1)


def dfs_height(node: Node) ->   int:
    """If the tree is balanced, returns its depth, otherwise returns -1."""
    if ( node is None ):
        return(0)  # base case
    leftHeight  = dfs_height(node.left)
    rightHeight = dfs_height(node.right)
    if ( (leftHeight == -1) or (rightHeight == -1) ):
        return(-1)  # one of subtrees is already unbalanced
    if ( abs(leftHeight - rightHeight) ) > 1:
        return(-1)  # the current (sub)tree itself is unbalanced
    return(1 + max(leftHeight, rightHeight))


def test__binary_tree_is_balanced():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ /
    ##  3  4 5
    t1n0 = Node(0)
    t1n1 = Node(1);    t1n2 = Node(2)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = Node(3);    t1n4 = Node(4);     t1n5 = Node(5)
    t1n1.left = t1n3;  t1n1.right = t1n4;  t1n2.left = t1n5
    ##     0
    ##      \
    ##       1
    ##        \
    ##         2
    t2n0 = Node(0)
    t2n1 = Node(1);    t2n2 = Node(2)
    t2n0.right = t2n1
    t2n1.right = t2n2
    ##     0
    t3n0 = Node(0)
    ##      0
    ##     /
    ##    1
    t4n0 = Node(0)
    t4n1 = Node(1)
    t4n0.left = t4n1


    for root in [t1n0, t2n0, t3n0, t4n0]:
        res = binary_tree_is_balanced(root)
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Tree by levels: {byLevels}")
        print(f"Result: {res}")

    
