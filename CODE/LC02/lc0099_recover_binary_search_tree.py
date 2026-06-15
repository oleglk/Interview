# lc0099_recover_binary_search_tree.py
# You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0099_recover_binary_search_tree import *

# RELOAD:
# import importlib; import lc0099_recover_binary_search_tree; importlib.reload(lc0099_recover_binary_search_tree); from lc0099_recover_binary_search_tree import *

# The idea: inorder traversal of BST yields ascending order. Any violation is a swap.
# adjacent swap: 1,2,3,4,5 => 1,2,4,3,5, broken pair: 4,3
# non-adjacent swap: 1,2,3,4,5 => 1,4,3,2,5, broken pairs: 4,3 and 3,2
# In any case need to swap the first (larger) node of the 1st broken pair with the second (smaller) node of the last broken pair.
# See https://algo.monster/liteproblems/99


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def recover_binary_search_tree(root: Node) -> None:
    def inorder(root: Node) -> None:
        """Searches for swapped nodes in the tree."""
        nonlocal prevNode, firstSwapped, lastSwapped
        if ( root is None ):
            return
        
        inorder(root.left)  # search for violations in the left subtree

        # check violation at the current node
        if ( prevNode and (prevNode.data > root.data) ):  # violation found
            if ( firstSwapped is None ):
                firstSwapped = prevNode  # assigned only once
            lastSwapped = root  # could be assigned once (adj) or twice (non-adj)

        prevNode = root

        inorder(root.right)  # search for violations in the right subtree
        return

    prevNode = None
    firstSwapped = None
    lastSwapped = None
    
    inorder(root)  # search for swapped nodes
    # perform the swap of node data
    firstSwapped.data, lastSwapped.data = lastSwapped.data, firstSwapped.data
    return
##


def test__recover_binary_search_tree():
    ####################################
    ##         2                3    
    ##        / \              / \   
    ##       3   4    ==>     2   4  
    ##      /     \          /     \ 
    ##     1       5        1       5
    t1n1 = Node(2); t1n2 = Node(3); t1n3 = Node(4); t1n4 = Node(1); t1n5 = Node(5)
    t1n1.left = t1n2;  t1n1.right = t1n3;  t1n2.left = t1n4;  t1n3.right = t1n5
    ####################################
    ##         3                3    
    ##        / \              / \   
    ##       5   4    ==>     2   4  
    ##      /     \          /     \ 
    ##     1       2        1       5
    t2n1 = Node(3); t2n2 = Node(5); t2n3 = Node(4); t2n4 = Node(1); t2n5 = Node(2)
    t2n1.left = t2n2;  t2n1.right = t2n3;  t2n2.left = t2n4;  t2n3.right = t2n5

    for root in [t1n1, t2n1]:
        print("==============================================")
        byLevels1 = binary_tree_level_order(root)
        print(f"Original tree by levels: {byLevels1}")
        recover_binary_search_tree(root)
        byLevels2 = binary_tree_level_order(root)
        print(f"Recovered BST by levels: {byLevels2}")
##

