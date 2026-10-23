# lc0188__best_time_to_buy_and_sell_stock_4.py
# You are given an integer array prices where prices[i] is the price of a given stock on the i-th day, and an integer k.
# Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0188__best_time_to_buy_and_sell_stock_4 import *

# RELOAD:
# import importlib;    import lc0188__best_time_to_buy_and_sell_stock_4;  importlib.reload(lc0188__best_time_to_buy_and_sell_stock_4);  from lc0188__best_time_to_buy_and_sell_stock_4 import *

# The idea: recursive DP with memoization. On each day there are up to 3 options:
# (1) do nothing
# (2) if not holding stock, buy it
# (3) if holding stock, sell it
# Need to keep track of 2 states: (a) whether holding stock, (b) how many transactions are left.
# See: https://algo.monster/liteproblems/188

from functools import cache

def best_time_to_buy_and_sell_stock_4(prices: list[int], k: int) -> int:
    @cache
    def best_time_recurse(dayIdx: int, transactonsLeft: int, holdStock: bool) -> int:
        if ( dayIdx >= len(prices) ):
            return 0  # time ran out, cannot make more profit
        # compute and compare the 3 options for remaining days
        # option of doing nothing at #dayIdx
        maxProfit = 0 + best_time_recurse(dayIdx+1, transactonsLeft, holdStock)
        if ( holdStock ):
            # option of selling stock at #dayIdx
            maxProfit = max(maxProfit, prices[dayIdx] + \
                best_time_recurse(dayIdx+1, transactonsLeft, False))
        elif ( transactonsLeft > 0 ):
            # option of buying stock at #dayIdx
            maxProfit = max(maxProfit, -prices[dayIdx] + \
                best_time_recurse(dayIdx+1, transactonsLeft-1, True))
        return maxProfit
    ##
    return best_time_recurse(0, k, False)
##


def test__best_time_to_buy_and_sell_stock_4():
    tasks = [
        [[2,4,1], 2],       # 2
        [[3,2,6,5,0,3], 2], # 7
    ]
    for  prices, k  in tasks:
        print("=======================================")
        print(f"Input: {prices}, {k}")
        res = best_time_to_buy_and_sell_stock_4(prices, k)
        print(f"Result: {res}")
##
