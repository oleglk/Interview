# lc0048__rotate_image.py
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# 123
# 456
# 789
# \/
# 741
# 852
# 963
# #0,0 -> #0,2;  #0,1 -> #1,2;  #0,2 -> 2,2
# #2,0 -> #0,0;  #2,1 -> #1,0;  #2,2 -> 2,0
# #i,j -> #j,n-i-1

# The idea: flip horizontally then transpose.
# See: https://algo.monster/liteproblems/48
# Horizontal flip: #i,j     -> #n-i-1,j
# Transposition:   #n-i-1,j -> #j,n-i-1

