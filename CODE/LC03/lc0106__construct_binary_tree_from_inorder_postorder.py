# lc0106__construct_binary_tree_from_inorder_postorder.py
# Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0106__construct_binary_tree_from_inorder_postorder import *

# RELOAD:
# import importlib;    import lc0106__construct_binary_tree_from_inorder_postorder;  importlib.reload(lc0106__construct_binary_tree_from_inorder_postorder);  from lc0106__construct_binary_tree_from_inorder_postorder import *

# The idea: recursively build subtrees by knowing their boundary indices in the two arrays.
# See https://algo.monster/liteproblems/106


from UTILS.lib__binary_tree_level_order_traversal import *  # for "visualization"

# class Node defined in lib__binary_tree_level_order_traversal.py
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None  # Reference to the left child node
#         self.right = None # Reference to the right child node
####


def construct_binary_tree_from_inorder_postorder(inorder: list[int], \
                                                 postorder: list[int]) -> \
                                                 Node|None:
    if ( (len(inorder) == 0) or (len(postorder) == 0) ):
        return None
    
    def make_subtree(inorderStart: int, postorderStart: int, subtreeSize: int) \
            -> Node|None:
        # base case
        if ( subtreeSize <= 0 ):
            return None

        rootVal = postorder[postorderStart + subtreeSize - 1]  # root is last
        rootIdxInInorder = inorderIdxMap[rootVal]
        leftSubtreeSize = rootIdxInInorder - inorderStart

        leftSubtree = make_subtree(inorderStart, \
                                   postorderStart, \
                                   leftSubtreeSize)

        rightSubtree = make_subtree(inorderStart + leftSubtreeSize + 1, \
                                    postorderStart + leftSubtreeSize, \
                                    subtreeSize - leftSubtreeSize - 1)

        root = Node(rootVal)
        root.left = leftSubtree
        root.right = rightSubtree
        return root
    ##

    inorderIdxMap = {val: idx for idx, val in enumerate(inorder)}
    return make_subtree(0, 0, len(inorder))
##


def postorder_traversal(root: Node) -> list[int]:
    result = []
    def postorder_recurse(root: Node) -> None:
        nonlocal result
        if ( root is not None ):
            postorder_recurse(root.left)
            postorder_recurse(root.right)
            result.append(root.data)
        else:
            result.append(None)
    ##
    postorder_recurse(root)
    return result
##
    

def test__construct_binary_tree_from_postorder_inorder():
    tasks = [
        [[9,3,15,20,7], [9,15,7,20,3]],
        [[-1], [-1]]
        ]

    for inorder, postorder in tasks:
        print("==========================================")
        print(f"Inorder: {inorder}, Postorder: {postorder}")
        resRoot = construct_binary_tree_from_inorder_postorder(inorder, postorder)
        byLevels = binary_tree_level_order(resRoot)
        print(f"Result by levels: {byLevels}")
        resultPostorder = postorder_traversal(resRoot)
        print(f"Result postorder = {resultPostorder}")
##
