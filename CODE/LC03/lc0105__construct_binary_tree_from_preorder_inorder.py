# lc0105__construct_binary_tree_from_preorder_inorder.py
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0105__construct_binary_tree_from_preorder_inorder import *

# RELOAD:
# import importlib;    import lc0105__construct_binary_tree_from_preorder_inorder;  importlib.reload(lc0105__construct_binary_tree_from_preorder_inorder);  from lc0105__construct_binary_tree_from_preorder_inorder import *

# The idea: recursively build subtrees by knowing their boundary indices in the two arrays.
# See https://algo.monster/liteproblems/105


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def construct_binary_tree_from_preorder_inorder(preorder: list[int], \
                                                inorder: list[int]) -> Node|None:
    def make_subtree(preorderStart: int, inorderStart: int, \
                     subtreeSize: int) -> Node|None:
        # base case
        if ( subtreeSize <= 0 ):
            return None
        
        rootVal = preorder[preorderStart]  # root comes 1st in preorder
        rootIdxInInorder = inorderIdxMap[rootVal]
        # left subtree begins at 'inorderStart' and ends before root index
        leftSubtreeSize = rootIdxInInorder - inorderStart
        
        leftSubtreeRoot = make_subtree(preorderStart + 1, \
                                       inorderStart, \
                                       leftSubtreeSize)

        # right subtree starts after root and left subtree
        rightSubtreeRoot = make_subtree(preorderStart + 1 + leftSubtreeSize, \
                                        rootIdxInInorder + 1, \
                                        subtreeSize - 1 - leftSubtreeSize)

        root = Node(rootVal)
        root.left = leftSubtreeRoot
        root.right = rightSubtreeRoot
        return root
    ##

    inorderIdxMap = {val: idx for idx, val in enumerate(inorder)}
    
    return make_subtree(0, 0, len(preorder))
##


def preorder_traversal(root: Node) -> list[int]:
    result = []
    def preorder_recurse(root: Node) -> None:
        nonlocal result
        if ( root is not None ):
            result.append(root.data)
            preorder_recurse(root.left)
            preorder_recurse(root.right)
        else:
            result.append(None)
    ##
    preorder_recurse(root)
    return result
##
    

def test__construct_binary_tree_from_preorder_inorder():
    tasks = [
        [[3,9,20,15,7], [9,3,15,20,7]],
        [[-1], [-1]]
        ]

    for preorder, inorder in tasks:
        print("==========================================")
        print(f"Preorder: {preorder},  Inorder: {inorder}")
        resRoot = construct_binary_tree_from_preorder_inorder(preorder, inorder)
        byLevels = binary_tree_level_order(resRoot)
        print(f"Result by levels: {byLevels}")
        resultPreorder = preorder_traversal(resRoot)
        print(f"Result preorder = {resultPreorder}")
##
