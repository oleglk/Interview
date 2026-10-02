# lc0157__read_n_chars_given_read4.py
# Implement a read method that reads n characters from a file, but you can only access the file through a provided read4 API.
# The read4 API works as follows:
#     It reads exactly 4 consecutive characters from the file (or fewer if the file has less than 4 characters remaining)
#     It stores these characters in a buffer array buf4 that you pass to it
#     It returns the number of characters actually read (0-4)
#     It maintains its own file pointer that advances as it reads
# Your task is to implement the read(buf, n) method that:
#     Reads exactly n characters from the file (or fewer if the file has less than n characters)
#     Stores these characters in the provided buffer buf
#     Returns the number of characters actually read

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0157__read_n_chars_given_read4 import *

# RELOAD:
# import importlib;    import lc0157__read_n_chars_given_read4;  importlib.reload(lc0157__read_n_chars_given_read4);  from lc0157__read_n_chars_given_read4 import *

# The idea: read chunks of (up to) 4 into temporary buffer, copy one-by-one into output buffer until required count achieved.
# See: https://algo.monster/liteproblems/157


def read_n_chars_given_read4(buf: list[str], n: int) -> int:
    tmpBuf = [''] * 4
    buf = ''
    cntCopied = 0
    cntRead = 4  # to enter the following loop
    # (while last read didn't encounter EOF ...)
    while ( cntRead == 4 ):
        cntRead = read4(tmpBuf)
        # copy into the output buffer up to required count
        for i in range(cntRead):
            if ( cntCopied >= n ):
                return n  # break if required count achieved
            buf[cntCopied] = tmpBuf[i]
            cntCopied += 1
    return cntCopied
##
