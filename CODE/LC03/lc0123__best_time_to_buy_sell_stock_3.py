# lc0123__best_time_to_buy_sell_stock_3.py
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete at most two transactions.
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0123__best_time_to_buy_sell_stock_3 import *

# RELOAD:
# import importlib;    import lc0123__best_time_to_buy_sell_stock_3;  importlib.reload(lc0123__best_time_to_buy_sell_stock_3);  from lc0123__best_time_to_buy_sell_stock_3 import *

# The idea: recursion with the following parameters: dayIndex, buyOrCellState, numTransactionsLeft. On each day choose best btw performing and not performing the permitted action (buy or cell).
# See https://codeanddebug.in/blog/best-time-to-buy-and-sell-stock-iii/


def best_time_to_buy_sell_stock_3(prices: list[float]) -> float:
    def best_time_recurse(prices: list[float], dayIdx: int, \
                          canBuy: bool, limit: int, \
                          memo: list[list[list[int]]]) -> float:
        # base cases
        if ( dayIdx >= len(prices) ):
            return 0  # time ended - cannot earn more
        if ( limit == 0 ):
            return 0  # limit of transactions exhausted - cannot earn more

        if ( memo[dayIdx][canBuy][limit] != -1 ):
            return memo[dayIdx][canBuy][limit]

        # recursive cases
        if ( canBuy ):  # either buy or not
            # (limit reduces only after sell completed)
            profitDoBuy = -prices[dayIdx] + \
                best_time_recurse(prices, dayIdx+1, False, limit, memo)
            profitNoBuy = 0 + \
                best_time_recurse(prices, dayIdx+1, True,  limit, memo)
            profit = max(profitDoBuy, profitNoBuy)
        else:  # either sell or not
            profitDoSell = prices[dayIdx] + \
                best_time_recurse(prices, dayIdx+1, True,  limit-1, memo)
            profitNoSell = 0 + \
                best_time_recurse(prices, dayIdx+1, False, limit,   memo)
            profit = max(profitDoSell, profitNoSell)
        memo[dayIdx][canBuy][limit] = profit
        return profit
    ##
    n = len(prices)
    memo = [[[-1 for limit in range(3)] for canBuy in range(2)] \
            for dayIdx in range(n)]
    return best_time_recurse(prices, 0, True, 2, memo)
##


def test__best_time_to_buy_sell_stock_3():
    tasks = [
        [3,3,5,0,0,3,1,4],  # 6
        [1,2,3,4,5],        # 4
        [7,6,4,3,1],        # 0
    ]
    for prices in tasks:
        print("============================================")
        print(f"Input: {prices}")
        res = best_time_to_buy_sell_stock_3(prices)
        print(f"Result: {res}")
##

