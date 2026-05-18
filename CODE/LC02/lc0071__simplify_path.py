# lc0071__simplify_path.py
# You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.
# The rules of a Unix-style file system are as follows:
#    A single period '.' represents the current directory.
#    A double period '..' represents the previous/parent directory.
#    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
#    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
# The simplified canonical path should follow these rules:
#   The path must start with a single slash '/'.
#   Directories within the path must be separated by exactly one slash '/'.
#   The path must not end with a slash '/', unless it is the root directory.
#   The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
# Return the simplified canonical path.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0071__simplify_path import *

# RELOAD:
# import importlib; import lc0071__simplify_path; importlib.reload(lc0071__simplify_path); from lc0071__simplify_path import *

# The idea: split path at '/', then feed into stack. Empty elements (caused by "//") and '.' are ignored, '..' causes pop unless the stack is empty, any other string is pushed into stack. When finished, prepend with '/' and join by '/'.
# See https://interviewing.io/questions/simplify-path


def simplify_path(pathStr: str) -> str:
    pathList = pathStr.split('/')
    stack = []
    
    for name in pathList:
        if ( (name == "") or (name == ".") ):
            continue
        elif ( name == ".." ):
            if ( len(stack) > 0 ):
                stack.pop()
            else:
                continue
        else:  # regular word means a subdirectory
            stack.append(name)

    return "/" + "/".join(stack)
##


def test__simplify_path():
    tasks = [
        "/home/",                               # "/home"
        "/home//foo/",                          # "/home/foo"
        "/home/user/Documents/../Pictures",     # "/home/user/Pictures"
        "/../",                                 # "/"
        "/.../a/../b/c/../d/./",                # "/.../b/d"
    ]
    for pathStr in tasks:
        print("==============================")
        print(f"Input: {pathStr}")
        res = simplify_path(pathStr)
        print(f"Result: {res}")
##
