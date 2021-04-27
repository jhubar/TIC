import numpy as np
from collections import Counter

class Hoffman_tree():
    def __init__(self, node_left =  None , node_right = None):
        self.node_left = node_left
        self.node_right = node_right

    def children(self):
        return (self.node_left, self.node_right)

    def nodes(self):
        return (self.node_left, self.node_right)

    def __str__(self):
        return '%s_%s' % (self.node_left, self.node_right)

class Huffman():

    def __init__(self, sequence):
        self.frequency = {}
        self.flag = True

        if(type(sequence) is list):
            if type(sequence[0]) is not str :
                sequence = np.array(sequence)
                self.frequency = dict(Counter(sequence))
                self.frequency = {str(k):int(v) for k,v in self.frequency.items()}
                self.flag = False


        self.sequence = sequence
        self.huffman_compression = {}

        self.nodes = {}
        self.huffman_code = []

    def huffman_code_tree(self, node, left=True, binString=''):
        if type(node) is str:
            return {node: binString}
        (l, r) = node.children()
        d = dict()
        d.update(self.huffman_code_tree(l, True, binString + '0'))
        d.update(self.huffman_code_tree(r, False, binString + '1'))
        return d

    def compute_frequency(self):

        for i in self.sequence:
            if i in self.frequency:
                self.frequency[i] += 1
            else:
                self.frequency[i] = 1

    def super_sort(self, dict = None, list = None):
        if dict != None:
            return sorted(dict.items(), key=lambda x: x[1], reverse=True)
        else:
            return sorted(list, key=lambda x: x[1], reverse=True)


    def create_tree(self):
        while len(self.nodes) > 1:
            (key_1, item_1) = self.nodes[-1]
            (key_2, item_2) = self.nodes[-2]
            self.nodes = self.nodes[:-2]
            node = Hoffman_tree(key_1, key_2)
            self.nodes.append((node, item_1 + item_2))

            self.nodes = self.super_sort(list = self.nodes)


    def run_hoffman_code(self):

        if self.flag == True:
            self.compute_frequency()
        # print(self.frequency)
        self.nodes = self.super_sort(dict = self.frequency)
        # print(self.nodes)
        self.create_tree()

        self.huffman_code = self.huffman_code_tree(self.nodes[0][0])




    def print_huffman_code(self):
        print(' Occurance | Huffman code ')
        print('--------------------------')
        for (item, code) in self.super_sort(dict = self.frequency):
            print(' %-6r    |%14s' % (item, self.huffman_code[item]))
