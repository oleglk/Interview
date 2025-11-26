# minimum_coins_recursive.py - Given coins of different denominations and a total amount, compute the fewest number of coins needed to make up that amount. If it's not possible, return -1. Recursive solution.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from minimum_coins_recursive import *

# RELOAD:
# import importlib;    import minimum_coins_recursive;  importlib.reload(minimum_coins_recursive);  from minimum_coins_recursive import *

# The idea: for each coin-value min_coins = min(1 + min_coins(sum - coinVal))
# (see: https://afteracademy.com/blog/minimum-coin-change/)


minCoinsMemo = {}

def _minimum_coins_recursive(coins: list, sum: int) -> int:
    if ( sum = 0 ):
        return(0)
    minCoins = 999999
    for coin in coins:
        if ( coin <= sum ):
            if ( (sum-coin) in minCoinsMemo ):
                currMin = minCoinsMemo[sum-coin]
            else:
                currMin = _minimum_coins_recursive(coins, sum-coin)
            minCoins = min(minCoins, 1 + currMin)
    return(minCoins)


def run_minimum_coins_recursive(coins: list, sum: int) -> int:
    minCoinsMemo = {}
    return(_minimum_coins_recursive(coins, sum)
