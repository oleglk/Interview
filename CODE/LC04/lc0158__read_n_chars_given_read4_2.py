# lc0158__read_n_chars_given_read4_2.py
# Implement a file reading system using a provided API called read4. The read4 API reads up to 4 characters from a file and writes them into a buffer. Your task is to implement a read method that can be called multiple times, each time reading up to n characters into a given buffer.
# The catch is that you must correctly handle the situation where the read method is called several times in a row, possibly reading partial data from the file each time, and not skipping or duplicating any characters.

# LOAD:
# import sys;  import os;  sys.path.insert(0, os.getcwd());  from lc0158__read_n_chars_given_read4_2 import *

# RELOAD:
# import importlib;    import lc0158__read_n_chars_given_read4_2;  importlib.reload(lc0158__read_n_chars_given_read4_2);  from lc0158__read_n_chars_given_read4_2 import *

# The idea:
# Maintain temp buffer with readIdx and nChars (num of chars read by read4)
# In the cycle of writeIdx < n:
# - refill the temporary buffer if needed
# - copy from temporary- to output buffer while checking (writeIdx < n)
# See: https://algomap.io/question-bank/read-n-characters-given-read4-ii-call-multiple-times


class ReadBy4:
    def __init__(self):
        self.buf = [''] * 4  # temporary buffer
        self.readIdx = 0     # current read index in the temporary buffer
        self.nChars = 0      # number of characters in the temporary buffer
    ##


    def read(outBuf: list[str], n: int) -> int:
        writeIdx = 0  # current index in the output buffer
        while ( writeIdx < n ):
            # refill temp buffer if it's empty or fully read-from
            if ( self.readIdx == self.nChars ):
                self.nChars = read4(self.buf)
                self.readIdx = 0
                if ( self.nChars == 0 ):
                    break  # EOF
            # copy from temporary- to output buffer
            # output buffer has either leftover or just read characters
            while ( (writeIdx < n) and (self.readIdx < self.nChars) ):
                outBuf[writeIdx] = self.buf[self.readIdx]
                writeIdx += 1
                self.readIdx += 1
        return writeIdx
    ##
####
