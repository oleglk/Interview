# minimum_coins_recursive.py - Given coins of different denominations and a total amount, compute the fewest number of coins needed to make up that amount. If it's not possible, return -1. Recursive solution.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from minimum_coins_recursive import *

# RELOAD:
# import importlib;    import minimum_coins_recursive;  importlib.reload(minimum_coins_recursive);  from minimum_coins_recursive import *

# The idea: for each coin-value min_coins = min(1 + min_coins(sum - coinVal))
# (see: https://www.stratascratch.com/blog/solving-leetcode-coin-change-problem-for-data-science-interviews/)

class Solution:
    positiveInf = 999999
    def __init__(self, coins: list, sum: int):
        self.minCoinsMemo = {}
        self.coins = coins
        self.target = sum
        self.coins.sort()  # ascending


    def _minimum_coins_recursive(self, sum: int) -> int:
        if ( sum == 0 ):
            return(0)
        if ( sum in self.minCoinsMemo ):
            return(self.minCoinsMemo[sum])
               
        minCoins = Solution.positiveInf
        for coin in self.coins:
            if ( coin > sum ):
                break  # this coin too large, others even larger due to sort
            currMin = _minimum_coins_recursive(sum-coin)
            minCoins = min(minCoins, 1 + currMin)
        self.minCoinsMemo[sum] = minCoins
        return(minCoins)

    
    @staticmethod
    def run_minimum_coins_recursive(coins: list, sum: int) -> int:
        sln = Solution()
        res = _minimum_coins_recursive(self.target)
        return(res if (res != Solution.positiveInf)  else  -1)


def test__minimum_coins_recursive():
    coins = [1, 3, 5, 10]
    sums = [1, 2, 6, 9, 13, 16]
    for sum in sums:
        print("====possible==========")
        print(f"Coins: {coins}, target: {sum}")
        res = run_minimum_coins_recursive(coins, sum)
        print(f"   => num-coins: {res}")
    # impossible cases
    coins = [3, 5, 10];
    sums = [1, 2, 4, 7]
    for sum in sums:
        print("====impossible========")
        print(f"Coins: {coins}, target: {sum}")
        res = run_minimum_coins_recursive(coins, sum)
        print(f"   => num-coins: {res}")
