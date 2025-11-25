# binary_search_tree_lowest_common_ancestor.py - Given a Binary Search Tree (BST) and two nodes p and q, find their lowest common ancestor (LCA).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_search_tree_lowest_common_ancestor import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import binary_search_tree_lowest_common_ancestor;  importlib.reload(binary_search_tree_lowest_common_ancestor);  from binary_search_tree_lowest_common_ancestor import *

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


def binary_search_tree_lowest_common_ancestor(root: Node,
                                              p: Node, q: Node) -> Node:
    """Returns LCA of 'p' and 'q' in BST rooted at 'root'"""
    node = root
    while ( node is not None ):
        if ( (p.data < node.data) and (q.data < node.data) ):
            node = node.left   ## descend into left subtree
        if ( (p.data > node.data) and (q.data > node.data) ):
            node = node.right  ## descend into right subtree
        else:
            return(node)
    

def test__binary_search_tree_lowest_common_ancestor():
    ##      5
    ##     / \
    ##    2   7
    ##   / \ / \
    ##  1  3 6  8
    t1n1 = Node(1);  t1n2 = Node(2);  t1n3 = Node(3);  t1n5 = Node(5);  
    t1n6 = Node(6);  t1n7 = Node(7);  t1n8 = Node(8)
    t1n5.left = t1n2;  t1n5.right = t1n7
    t1n2.left = t1n1;  t1n2.right = t1n3
    t1n7.left = t1n6;  t1n7.right = t1n8

    root = t1n5
    byLevels = binary_tree_level_order(root)
    print(f"Tree by levels: {byLevels}")
    print(f"--- Calls with valid root ---")
    for n1, n2  in  [[t1n2,t1n7], [t1n1,t1n3], [t1n1,t1n6], [t1n3,t1n8],
                     [t1n6,t1n8]]:
        lca = binary_search_tree_lowest_common_ancestor(root, n1, n2)
        print(f"(root:{root.data}) {n1.data}, {n2.data}  -> LCA:{lca.data}")
    print(f"--- Calls with invalid root ---")
    for n1, n2  in  [[t1n1,t1n3], [t1n3,t1n8], [t1n6,t1n8]]:
        lca = binary_search_tree_lowest_common_ancestor(t1n1, n1, n2)
        print(f"(root:{Node.fmt(t1n1)}) {Node.fmt(n1)}, {Node.fmt(n2)}  -> LCA:{Node.fmt(lca)}")
