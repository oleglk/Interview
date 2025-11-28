# minimum_coins_iterative.py - Given coins of different denominations and a total amount, compute the fewest number of coins needed to make up that amount. If it's not possible, return -1. Recursive solution.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from minimum_coins_iterative import *

# RELOAD:
# import importlib;    import minimum_coins_iterative;  importlib.reload(minimum_coins_iterative);  from minimum_coins_iterative import *

# The idea: for each coin-value min_coins = min(1 + min_coins(sum - coinVal))
# (see: https://afteracademy.com/blog/minimum-coin-change/)


positiveInf = 999999

def minimum_coins_iterative(coins: list, sum: int) -> int:
    minCoinsArr = [positiveInf] * (sum+1)  # num of coins for amounts 0..sum
    minCoinsArr[0] = 0  # no coins for sum of 0

    for coin in coins:
        for amount in range(coin, sum+1):
            # update 'minCoinsArr' with amounts reachable with current coin
            minCoinsArr[amount] = min(minCoinsArr[amount],
                                      minCoinsArr[amount - coin] + 1)
    
    return(minCoinsArr[sum] if (minCoinsArr[sum] != positiveInf)  else  -1)


def test__minimum_coins_iterative():
    coins = [1, 3, 5, 10]
    sums = [1, 2, 6, 9, 13, 16]
    for sum in sums:
        print("====possible==========")
        print(f"Coins: {coins}, target: {sum}")
        res = minimum_coins_iterative(coins, sum)
        print(f"   => num-coins: {res}")
    # impossible cases
    coins = [3, 5, 10];
    sums = [1, 2, 4, 7]
    for sum in sums:
        print("====impossible========")
        print(f"Coins: {coins}, target: {sum}")
        res = minimum_coins_iterative(coins, sum)
        print(f"   => num-coins: {res}")
