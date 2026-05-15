# lc0068__text_justification.py
# Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left-justified, and no extra space is inserted between words.
# Note:
#     A word is defined as a character sequence consisting of non-space characters only.
#    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
#    The input array words contains at least one word.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0068__text_justification import *

# RELOAD:
# import importlib; import lc0068__text_justification; importlib.reload(lc0068__text_justification); from lc0068__text_justification import *

# The idea: have 2 helper functions - pack_words_in_line() and format_line_with_spaces(); implement according to the spec.
# See https://algo.monster/liteproblems/68


def text_justify(words: list[str], maxWidth: int) -> list[str]:
    firstIdxInLine = 0  # index of the 1st word in the current line
    result = []         # for the resulting text
    while ( firstIdxInLine < len(words) ):
        lineWords = pack_words_in_line(words, firstIdxInLine, maxWidth)
        isLast = (firstIdxInLine + len(lineWords)) >= len(words)
        formatted = format_line_with_spaces(lineWords, isLast, maxWidth)
        result.append(formatted)
        firstIdxInLine += len(lineWords)
    return result
##


# Returns words to go into one line starting from word #'firstIdxInLine'
def pack_words_in_line(words: list[str], firstIdxInLine: int, maxWidth: int) -> list[str]:
    lineWords = [words[firstIdxInLine]]
    width = len(words[firstIdxInLine])
    for i in range(firstIdxInLine+1, len(words)):
        if ( (width + len(words[i]) + 1) <= maxWidth ): # consider word and space
            lineWords.append(words[i])
            width += len(words[i]) + 1
        else:
            break
    return lineWords
##


# Builds line from words in 'lineWords' with gaps as specified
def format_line_with_spaces(lineWords: list[str], isLast: int, maxWidth: int) -> str:
    lineStr = lineWords[0]
    if ( len(lineWords) == 1 ):  # all spaces in the end
        numTrailingSpaces = maxWidth - len(lineWords[0])
        lineStr += ' ' * numTrailingSpaces
        return lineStr
    # regular line with several words, but could be the last one
    numNonSpaces = 0
    for word in lineWords:
        numNonSpaces += len(word)
    numSpaces = maxWidth - numNonSpaces
    numGaps = len(lineWords) - 1
    baseNumSpacesInGap = numSpaces // numGaps
    numExtraSpacesLeft = numSpaces % numGaps
    if ( isLast ):  # special case - all extra spaces go to the end
        numExtraSpacesLeft = 0
    # append gaps and words
    for word in lineWords[1:]:
        gapLen = baseNumSpacesInGap + 1 if (numExtraSpacesLeft > 0) else baseNumSpacesInGap
        if ( isLast ):
            gapLen = 1  # special case - all extra spaces go to the end
        numExtraSpacesLeft -= 1  # ok to become < 0
        lineStr += ' ' * gapLen
        lineStr += word
    # in the last line apppend all extra spaces
    if ( isLast ):
        lineStr += ' ' * (maxWidth - len(lineStr))

    return lineStr
##


def test__text_justify():
    tasks = [
        [["This", "is", "an", "example", "of", "text", "justification."], 16],
        [["What","must","be","acknowledgment","shall","be"], 16],
        [["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20],
    ]
    for words, maxWidth  in tasks:
        print("========================================")
        print(f"Input: {words}, {maxWidth}")
        res = text_justify(words, maxWidth)
        print(f"Result:")
        for line in res:
            print(f"'{line}'")
##
