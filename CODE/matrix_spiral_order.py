# matrix_spiral_order.py - Return matrix elements in spiral order using boundaries.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from matrix_spiral_order import *

# RELOAD:
# import importlib; import matrix_spiral_order; importlib.reload(matrix_spiral_order); from matrix_spiral_order import *


# The idea: maintain 4 "wall" indices (top, right, bottom, left) and traverse along these walls while counting steps. After each pass along particular wall its index is updated.


def matrix_spiral_order(matrix: list) -> list:
    if ( (matrix is None) or (len(matrix) == 0) ):
        return([])
    nRows = len(matrix)
    nCols = len(matrix[0])
    nElements = nRows * nCols
    res = []
    STEPS_LEFT = 100

    # init walls to matrix outer boundaries
    top = 0;  bottom = nRows-1;  left = 0;  right = nCols-1
    while ((len(res) < nElements) and (STEPS_LEFT > 0)):
        STEPS_LEFT -= 1
        print(f"@@ top={top}, bottom={bottom}, left={left}, right={right}")
        # traverse top wall left to right
        for j in range(left, right+1, 1):
            res.append(matrix[top][j]);     print(f"@@ Append #{top},{j}")
        top += 1
        # traverse right wall top to bottom
        for i in range(top, bottom+1, 1):
            res.append(matrix[i][right]);   print(f"@@ Append #{i},{right}")
        right -= 1
        # traverse bottom wall right to left
        for j in range(right, left-1, -1):
            res.append(matrix[bottom][j]);  print(f"@@ Append #{bottom},{j}")
        bottom -= 1
        # traverse left wall bottom to top
        for i in range(bottom, top-1, -1):
            res.append(matrix[i][left]);    print(f"@@ Append #{i},{left}")
        left += 1
    return(res)


def test__matrix_spiral_order():
    m1 = [[1]]
    m2 = [[1,2,3], [4,5,6], [7,8,9]]
    m3 = [[1,2], [3,4], [5,6], [7,8]]
    for m in [m1, m2, m3]:
        print("=================================")
        print(f"Input: {m}")
        res = matrix_spiral_order(m)
        print(f"Result: {res}")
