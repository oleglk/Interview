# graph_serialize_deserialize.py - Serialize an undirected graph to string and deserialize back.
## Assumptions: - graph represented by adjacency lists dictionary:
##                {nodeId :: list-of-adjacent-nodeIds}
##              - nodeId-s are unique

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from graph_serialize_deserialize import *

# RELOAD:
# import importlib; import graph_serialize_deserialize; importlib.reload(graph_serialize_deserialize); from graph_serialize_deserialize import *


def graph_serialize(adjLists: dict) -> str:
    """'adjLists' is dict {vertex :: list-of-neighbours}.
       Returns representation string like:
       ID1:ID2,ID3|ID2:ID1,ID4|..."""
    res = ""
    for nodeId in adjLists:
        neighbourStrings = [str(x) for x in adjLists[nodeId]]
        if ( res != "" ):
            res += '|'  # delimit one-node records
        res += f"{str(nodeId)}:{','.join(neighbourStrings)}"  # one-node record
    return(res)


def graph_deserialize(repr: str) -> dict:
    """'repr' is ID1:ID2,ID3|ID2:ID1,ID4|...
       Returns adjacency-list dictionary {vertex :: list-of-neighbours}."""
    #print(f"@@ deserializing repr = '{repr}'")
    if ( repr == "" ):
        return({})
    adjLists = {}
    nodeRecordsStrList = repr.split('|')  # list of "ID1:ID2,ID3"
    #print(f"@@ deserializing nodeRecordsStrList = {nodeRecordsStrList}")
    for oneNodeRecordStr in nodeRecordsStrList:
        #print(f"@@ deserializing oneNodeRecordStr = '{oneNodeRecordStr}'")
        node, neighboursStr = oneNodeRecordStr.split(':')
        neighbours = neighboursStr.split(',')
        adjLists[node] = neighbours

    return(adjLists)


def test__graph_serialize_deserialize():
    # 1
    g1 = {1:[]}
    # 1-2
    g2 = {1:[2], 2:[1]}
    # 1-2-3
    #  \ /
    #   4
    g3 = {1:[2,4], 2:[1,3], 3:[2,4], 4:[1,3]}
    for g in [g1, g2, g3]:
        print("==========================================")
        print(f"Input: {g}")
        ser1 = graph_serialize(g)
        print(f"Serialized-1: {ser1}")
        deser = graph_deserialize(ser1)
        print(f"Deserialized: {deser}")
        ser2 = graph_serialize(deser)
        print(f"Serialized-2: {ser2}")
