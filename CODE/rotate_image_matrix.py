# rotate_image_matrix.py - Rotate n x n matrix in-place by transpose + reverse rows.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from rotate_image_matrix import *

# RELOAD:
# import importlib; import rotate_image_matrix; importlib.reload(rotate_image_matrix); from rotate_image_matrix import *


def rotate_image_matrix(matrix: list[list]) -> list[list]:
    n = len(matrix)
    if ( (n == 0) or (len(matrix[0]) != n) ):
        raise Exception("Invalid matrix")
    # transpose
    for i in range(0, n):
        for j in range(i+1, n):  # above main diagonal to exchange only once
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reverse rows
    for i in range(0, n):
        matrix[i].reverse()
    return(matrix)


def test__rotate_image_matrix():
    tasks = [ [[1]],  [[1,2],[3,4]], [[1,2,3],[4,5,6],[7,8,9]] ]
    for m in tasks:
        print("=================================")
        print(f"Input: {m}")
        res = rotate_image_matrix(m)
        print(f"Result: {res}")

# 12
# 34
# \/
# 13
# 24
# \/
# 31
# 42

# 123
# 456
# 789
# \/
# 147
# 258
# 369
# \/
# 741
# 852
# 963
