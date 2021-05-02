import numpy as np
from huffman import *
from LZ77 import *
import config

class Lempel_zip():

    def __init__(self,sequence):

        self.sequence = sequence
        self.position = []
        self.sub_sequence = []
        self.binary_encoded= []
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

        self.position = [i for i in range(1,len(list(self.keys)))]
        # print(self.position)
        # print(list(self.keys))
        self.sub_sequence = list(self.keys)

    def suffix_factoring(self,suffix):
        if suffix == '1' or suffix == 'A':
            suffix = 1
        else:
            suffix = 0
        return str(suffix)

    def prefix_factoring(self,prefix):
        return str(bin(prefix))

    def code_representation(self):
        tmp = []
        for i in range(len(self.sub_sequence)):
            if len(self.sub_sequence[i]) == 1:
                suffix = self.sub_sequence[i]
                suffix = self.suffix_factoring(suffix)

                prefix = self.prefix_factoring(0)

                tmp.append(prefix+suffix)
            else:
                suffix = self.sub_sequence[i][-1]
                suffix = self.suffix_factoring(suffix)

                prefix =  self.sub_sequence[i][:-1]
                prefix = self.sub_sequence.index(prefix)
                prefix = self.prefix_factoring(prefix)

                tmp.append(prefix+suffix)
        self.binary_encoded = tmp
        # print(tmp)
        return self.binary_encoded


    def binary_adddress(self):
        print("")

def binarize(v, nb=0):
    if nb == 0:
        return bin(v)[2:]
    else:
        return np.binary_repr(v,width=nb)

def binary_genome(input):
    f = input
    binary_text = ''
    for c in f:
    	binary_text = binary_text + binarize(ord(c),nb=8)
    return binary_text[1:]
