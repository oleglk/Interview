# edit_distance_recursive.py - Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2 (insert, delete, replace).

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from edit_distance_recursive import *

# RELOAD:
# import importlib; import edit_distance_recursive; importlib.reload(edit_distance_recursive); from edit_distance_recursive import *


# The idea: recursion from the right ends. Choose btw 4 possibilities:
# - if w1[m-1] == w2[n-1], recurse(m-1, n-1)
# - if w1[m-1] != w2[n-1], try delete w1[m-1] and recurse(m-1, n)
# - if w1[m-1] != w2[n-1], try insert w2[n-1] as w1[m] and recurse(m, n-1)
##                     (we made w1[m] match w2[n-1], now compare left of it)
# - if w1[m-1] != w2[n-1], try replace w1[m-1] by w2[n-1] and recurse(m-1, n-1)


def edit_distance_recurse(word1, word2, m, n, memo):
    if ( m == 0 ):
        #print(f"@@ at{m},{n}: m=0, return({n})")
        return(n)  # need to insert the whole of 'word2'
    if ( n == 0 ):
        #print(f"@@ at{m},{n}: n=0, return({m})")
        return(m)  # need to delete the whole of 'word1'

    if ( memo[m][n] != -1 ):
        return(memo[m][n])
    
    if ( word1[m-1] == word2[n-1] ):
        whenEqual = edit_distance_recurse(word1, word2, m-1, n-1, memo)
        memo[m][n] = whenEqual
        #print(f"@@ at{m},{n}: whenEqual m={m}, n={n} => {whenEqual}")
        return(whenEqual)

    # word1[m-1] != word2[n-1], choose min btw the 3 cases
    whenDeleted  = edit_distance_recurse(word1, word2, m-1, n,   memo)
    whenInserted = edit_distance_recurse(word1, word2, m,   n-1, memo)
    whenReplaced = edit_distance_recurse(word1, word2, m-1, n-1, memo)
    theMin = min(whenDeleted, whenInserted, whenReplaced)
    #print(f"@@ whenDeleted={whenDeleted}, whenInserted={whenInserted}, whenReplaced={whenReplaced} ==> {theMin}")
    memo[m][n] = 1 + theMin
    return(memo[m][n])


def edit_distance(word1, word2):
    n1 = len(word1)
    n2 = len(word2)
    memo = [[-1 for j in range(0, n2+1)] for i in range(0, n1+1)]
    return(edit_distance_recurse(word1, word2, n1, n2, memo))


def test__edit_distance():
    tasks = [ ["geek","gesek"], ["gfg","gfg"], ["abcd","bcfe"] ]
    #          1                 0              3
    for word1, word2 in tasks:
        print("===========================")
        print(f"Input: {word1}, {word2}")
        res = edit_distance(word1, word2)
        print(f"Result: {res}")
