# lc0077__combinations.py
# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0077__combinations import *

# RELOAD:
# import importlib; import lc0077__combinations; importlib.reload(lc0077__combinations); from lc0077__combinations import *


# The idea: recursion, for each number try including and not including it.

class Combinations:
    def __init__(self, n: int, k: int) -> None:
        self.n = n
        self.k = k
        self.result: list[list[int]] = []  # for resulting list of combinations
    

    def solve(self) -> list[list[int]]:
        currentCombo: list[int] = []
        self.recurse(1, currentCombo)
        return self.result


    def recurse(self, start: int, currentCombo: list[int]) -> None:
        # base case - valit combination completed
        if ( len(currentCombo) == self.k ):
            self.result.append(currentCombo[:])  # add copy of curr to result
            return
        # base case: numbers exhausted
        if ( start > self.n ):
            return

        # try with current starting number included
        currentCombo.append(start)
        self.recurse(start+1, currentCombo)

        # try with current starting number excluded
        currentCombo.pop()  # remove 'start' from current combo
        self.recurse(start+1, currentCombo)

        return
    ##


def test__Combinations():
    tasks = [
        [4, 2],  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        [1, 1],  # [[1]]
        [3, 2],  # [[1,2],[1,3],[2,3]]
    ]
    for n,k in tasks:
        print("======================================")
        print(f"Input: {n}, {k}")
        slv = Combinations(n, k)
        res = slv.solve()
        print(f"Result: {res}")
##

