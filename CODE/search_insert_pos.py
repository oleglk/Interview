# search_insert_pos.py

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from search_insert_pos import *

# RELOAD:
# import importlib;    import search_insert_pos;  importlib.reload(search_insert_pos);  from search_insert_pos import *


def search_insert_pos(arr: list, val: int):
    """Return index of 'val' in sorted 'arr' or its insert pos if not found."""
    if ( not arr ):
        return(0)
    lo = 0
    hi = len(arr) - 1
    while ( lo <= hi ):
        mid = (lo + hi) // 2
        print(f"@+ lo={lo}({arr[lo]}), mid={mid}({arr[mid]}), hi={hi}({arr[hi]})")
        if ( val == arr[mid] ):
            return(mid)   # 'val' appearance found
        elif ( val < arr[mid] ):
            hi = mid - 1  # continue in lower half
        else:
            lo = mid + 1  # continue in upper half
    # 'lo' > 'hi'; no 'val' appearance found
    print(f"@- lo={lo}, mid={mid} hi={hi}")
    # a hint why taking 'lo' (bigger): both can go out of range, but '-1' isn't an answer, while 'length' is fine
    return(lo)


def test__search_insert_pos():
    arr1 = [1,3,5,7]
    arr2 = [8,10]
    arr3 = [1,2,3,7,8]
    v1 = 3
    v2 = 8
    v3 = 4
    for arr in [arr1, arr2, arr3]:
        for v in [v1, v2, v3]:
            print("==========================")
            print(f"Array={arr},  val={v}")
            i = search_insert_pos(arr, v)
            print(f"Resulting index: {i}")
