# binary_tree_serialize_deserialize.py - Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization should work.


# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from binary_tree_serialize_deserialize import *

# RELOAD:
# import importlib;    import binary_tree_level_order_traversal;  importlib.reload(binary_tree_level_order_traversal);  from binary_tree_level_order_traversal import *;    import binary_tree_serialize_deserialize;  importlib.reload(binary_tree_serialize_deserialize);  from binary_tree_serialize_deserialize import *


# The idea: TODO

from binary_tree_level_order_traversal import *  # for "visualization"

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child node
        self.right = None # Reference to the right child node
##


def serialize(root: Node) -> str:
    nodeValsList = []

    def dfs_serialize_preorder(node):
        """Works on 'nodeValsList'"""
        if ( node is None ):
            nodeValsList.append("#")
            return
        nodeValsList.append(str(node.data))
        dfs_serialize_preorder(node.left)
        dfs_serialize_preorder(node.right)

    dfs_serialize_preorder(root)
    return(" ".join(nodeValsList))


def deserialize(nodeValsStr: str) -> Node:
    nodeValsList = nodeValsStr.split()
    dsIter = iter(nodeValsList)  # accessible to dfs_deserialize_preorder()
    
    def dfs_deserialize_preorder() -> Node:
        """Works on 'dsIter'"""
        try:  # expect to stop at null nodes and not catch StopIteration
            val = next(dsIter)
        except StopIteration:
            print("*** Invalid tree structure")
            raise Exception("INVALID")
        if ( val == "#" ):
            return(None)# there was a missing child
        node = Node(int(val))
        node.left  = dfs_deserialize_preorder()
        node.right = dfs_deserialize_preorder()
        return(node)

    return(dfs_deserialize_preorder())


def test__binary_tree_serialize_deserialize():
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
    ##     0
    ##    / \
    ##   1   2
    ##        \
    ##         3
    t5n0 = Node(0)
    t5n1 = Node(1);    t5n2 = Node(2);    t5n3 = Node(3)
    t5n0.left = t5n1;  t5n0.right = t5n2
    t5n2.right = t5n3

    for root in [t1n0, t2n0, t3n0, t4n0, t5n0]:
        print("===============================")
        byLevels = binary_tree_level_order(root)
        print(f"Original tree by levels: {byLevels}")
        resSer1 = serialize(root)
        print(f"Serialized to (1): {resSer1}")
        dsRoot = deserialize(resSer1)
        byLevels = binary_tree_level_order(dsRoot)
        print(f"Deserialized tree by levels: {byLevels}")
        resSer2 = serialize(dsRoot)
        print(f"Serialized to (2): {resSer2}")
