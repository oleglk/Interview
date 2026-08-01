# lc0122__best_time_to_buy_sell_stock_2.py
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.
# Find and return the maximum profit you can achieve.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0122__best_time_to_buy_sell_stock_2 import *

# RELOAD:
# import importlib;    import lc0122__best_time_to_buy_sell_stock_2;  importlib.reload(lc0122__best_time_to_buy_sell_stock_2);  from lc0122__best_time_to_buy_sell_stock_2 import *

# The idea: max [rpfot achieved if buy-cell every time today's price is larger than yesterday's.
# See: https://techsauce.medium.com/best-time-to-buy-and-sell-stock-ii-popular-coding-interview-question-cc68026a0ff2


def best_time_to_buy_sell_stock_2(prices: list[float]) -> float:
    profit = 0.0
    for i in range(0, len(prices)-1):
        if ( prices[i+1] > prices[i] ):
            profit += prices[i+1] - prices[i]

    return profit
##


def test__best_time_to_buy_sell_stock_2():
    tasks = [
        [7,1,5,3,6,4],  # 7
        [1,2,3,4,5],    # 4
        [7,6,4,3,1],    # 0
    ]
    for prices in tasks:
        print("============================================")
        print(f"Input: {prices}")
        res = best_time_to_buy_sell_stock_2(prices)
        print(f"Result: {res}")
##
