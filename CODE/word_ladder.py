# word_ladder.py - Given beginWord, endWord and a word-list, find shortest transformation sequence length changing one letter at a time. All intermediate words including endWord but excluding beginWord must be in word-list. Possible characters: latin a...z. All words are same length.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from word_ladder import *

# RELOAD:
# import importlib; import word_ladder; importlib.reload(word_ladder); from word_ladder import *

# The solution copied from https://algo.monster/liteproblems/127
# The idea: make BFS while reaching words in word-list through trying all 26 possible characters position by position.


from collections import deque

def word_ladder(beginWord: str, endWord: str, wordList: list) -> int:
    availableWords = set(wordList)  # visited words will be deleted from it
    if ( endWord not in availableWords):
        return(0)  # no solution possible
    transformLevel = 1  # current number of changed characters +1
    queue = deque([beginWord])

    while ( queue ):
        transformLevel += 1  # start new transformation level
        numWordsOnLevel = len(queue)
        
        # try all words on the currrent change level
        for _ in range(0, numWordsOnLevel):
            word = queue.popleft()
            chars = list(word)  # for easier manipulation
        
            for pos in range(0, len(chars)):  # try all positions in word
                origChar = chars[pos]  # to restore later and to avoid check

                for letterIdx in range(0, 26):  # try all Latin letters at pos
                    chars[pos] = chr(ord('a') + letterIdx)
                    if ( chars[pos] == origChar ):
                        continue  # skip original - for clarity
                    newWord = ''.join(chars)
                    if ( newWord == endWord ):
                        return(transformLevel)  # result is reached
                    if ( newWord not in availableWords ):
                        continue  # skip "invalid" or visited word

                    # valid intermediate word is reached
                    print(f"@@ Reached '{newWord}' at level {transformLevel}")
                    queue.append(newWord)
                    availableWords.remove(newWord)  # mark "visited"

                # done with position 'pos'
                chars[pos] = origChar  # to maintain correct num of changes

    return(0)  # 'endWord' not reached


def test__word_ladder():
    t1 = ["as", "is", ["is"]]  # 2
    t2 = ["warm", "calm", ["carm", "calm", "done"]]  # 3
    t3 = ["hit", "cog", ["hot","dot","dog","lot","log","cog"]]  # 5
    t4 = ["toon", "plea", ["poon","plee","same","poie","plea","plie","poin"]]  # 7
    t5 = ["abcv", "ebad", ["abcd","ebad","ebcd","xyza"]]  # 4

    for  beginWord, endWord, wordList in [t1, t2, t3, t4, t5]:
        print("============================")
        print(f"Input: {beginWord}, {endWord},  {wordList}")
        res = word_ladder(beginWord, endWord, wordList)
        print(f"Result: {res}")
