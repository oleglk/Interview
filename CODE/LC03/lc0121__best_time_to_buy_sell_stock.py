# lc0121__best_time_to_buy_sell_stock.py
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0121__best_time_to_buy_sell_stock import *

# RELOAD:
# import importlib;    import lc0121__best_time_to_buy_sell_stock;  importlib.reload(lc0121__best_time_to_buy_sell_stock);  from lc0121__best_time_to_buy_sell_stock import *

# The idea: traverse left to right; maintain min_price and max_profit.
# See https://algo.monster/liteproblems/121


def best_time_to_buy_sell_stock(prices: list[float]) -> float:
    minPrice = float('inf')
    maxProfit = 0
    for dailyPrice in prices:
        # profit goes vs earlier buying price
        maxProfit = max(maxProfit, dailyPrice - minPrice)
        minPrice = min(minPrice, dailyPrice)
    return maxProfit
##


def test__best_time_to_buy_sell_stock():
    tasks = [
        [7,1,5,3,6,4],  # 5
        [7,6,4,3,1],    # 0
    ]
    for prices in tasks:
        print("============================================")
        print(f"Input: {prices}")
        res = best_time_to_buy_sell_stock(prices)
        print(f"Result: {res}")
##
