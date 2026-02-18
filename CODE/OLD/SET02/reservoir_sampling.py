# reservoir_sampling.py - Uniformly select one element from the stream of data.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from reservoir_sampling import *

# RELOAD:
# import importlib; import reservoir_sampling; importlib.reload(reservoir_sampling); from reservoir_sampling import *

# The idea: pick #i-s element with probability of 1/i .
# Correctness proved by induction.
# Base case - n = 1, thus p = 1 - OK
# Assume uniformity for stream size of n, check uniformity for n+1:
# - element #n+1 selected with probability 1/(n+1)
# - any previous element selected with probability 1/n * (1 - 1/(n+1))
## 1/n * (1 - 1/(n+1)) == 1/n * n/(n+1) == 1/(n+1) <<<< uniformity proven
#################################################################################
# Alternative proof (ChatGPT for "How to solve Uniform Reservoir Sampling software interview problem?"):
# - ASSUME THAT an element #j is selected when first seen with probability 1/j
# - Then, to remain being the choice it should not be replace by consequent elements up to n.
# - Probability of not being replaced by element #i == 1 - 1/i
## Total probability of element #j being selected and not replaced:
## p = 1/j * (1 - 1/(j+1)) * (1 - 1/(j+2)) * ... * (1 - 1/n) =
##   = 1/j * j/(j+1)       * (j+1)/(j+2)   * ... * (n-1)/n   = 1/n
# E.g. if we select each element #j in stream of size n with probability 1/j, the resulting distribution has probability 1/n which means uniform.
# Element #0 selected with probability 1, #1 with probability 1/2, and so on.
#################################################################################

import random

def reservoir_sampling(iterableStream):
    res = None
    for (i, x) in enumerate(iterableStream):
        if ( random.random() < 1/(i+1) ):  # i=0>p=1, i=1>p=1/2, ...
            res = x
    return res


def test__reservoir_sampling():
    stream = [0,1,2,3,4,5,6,7,8,9]
    freq = [0]*len(stream)
    print("=======================")
    for _ in range(0, len(stream)*100):
        res = reservoir_sampling(stream)
        freq[res] += 1
    print(f"Result: {freq}")

            
