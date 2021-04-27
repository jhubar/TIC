import numpy as np
from huffman import *
from LZ77 import *
import config

class Lempel_zip():

    def __init__(self,sequence):

        self.sequence = sequence
        self.sub_sequence = []
        self.keys = {}







    def create_sub_sequence(self):
        i = 0
        j = 1
        while True:
            if not (len(self.sequence) >= i+j):
                break
            sub_sequence = self.sequence[i:i + j]
            if sub_sequence in self.keys:
                j += 1
            else:
                self.keys[sub_sequence] = 0
                i += j
                j = 1

        print(list(self.keys))
