# binary_tree_lowest_common_ancestor.py - find lowest common ancestor of 2 nodes in general binary tree (not BST).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_lowest_common_ancestor import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import binary_tree_lowest_common_ancestor;  importlib.reload(binary_tree_lowest_common_ancestor);  from binary_tree_lowest_common_ancestor import *

from binary_tree_level_order_traversal import *  # for "visualization"


# The idea: based on BSD property that if both nodes are smaller/larger than parent-node, they are in the left/right subtree of the parent-node.

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node

    @staticmethod
    def fmt(node: Node):
        return(node.data if (node is not None) else "none")
##

# The idea: recursively search for either one of the nodes or the LCA in the both subtrees.
# In case one subtree has one node and other subtree has the other node:
#  - root node of the current subtree is the LCA
#  - the current subtree has the both nodes
#  - the other subtree has neither of the 2 nodes and its recursive call must return None
# If only one of the 2 nodes found in the current subtree:
#  - the other node must be elsewhere
#  - the LCA must be somewhere above

def binary_tree_lowest_common_ancestor(root: Node,
                                       p: Node, q: Node) -> Node:
    """Returns LCA of 'p' and 'q' in general binary tree rooted at 'root'"""
    # base cases
    if ( root is None ):
        return(None)
    if ( root == p ):
        return(p)  # node 'p' found in this subtree
    if ( root == q ):
        return(q)  # node 'q' found in this subtree

    leftNodeOrLCA  = binary_tree_lowest_common_ancestor(root.left,  p, q)
    rightNodeOrLCA = binary_tree_lowest_common_ancestor(root.right, p, q)

    if ( (leftNodeOrLCA is not None) and (rightNodeOrLCA is not None) ):
        return(root)            # 'root' is the LCA
    if ( (leftNodeOrLCA is not None) and (rightNodeOrLCA is None) ):
        return(leftNodeOrLCA)   # 'leftNodeOrLCA' is LCA or one of 2 nodes
    if ( (leftNodeOrLCA is None)     and (rightNodeOrLCA is not None) ):
        return(rightNodeOrLCA)  # 'rightNodeOrLCA' is LCA or one of 2 nodes

    # neither of the 2 nodes found in the current subtree
    return(None)


def test__binary_tree_lowest_common_ancestor():
    ##      0
    ##     / \
    ##    1   2
    ##   / \ / \
    ##  3  4 5  6
    t1n0 = Node(0)
    t1n1 = Node(1);    t1n2 = Node(2)
    t1n0.left = t1n1;  t1n0.right = t1n2
    t1n3 = Node(3);    t1n4 = Node(4);     t1n5 = Node(5);     t1n6 = Node(6)
    t1n1.left = t1n3;  t1n1.right = t1n4
    t1n2.left = t1n5;  t1n2.right = t1n6

    
    root = t1n0
    byLevels = binary_tree_level_order(root)
    print(f"Tree by levels: {byLevels}")
    print(f"--- Calls with valid root ---")
    for n1, n2  in  [[t1n1,t1n2], [t1n3,t1n4], [t1n5,t1n6], [t1n3,t1n5]]:
        lca = binary_tree_lowest_common_ancestor(root, n1, n2)
        print(f"(root:{Node.fmt(root)}) {Node.fmt(n1)}, {Node.fmt(n2)}  -> LCA:{Node.fmt(lca)}")

