import numpy as np
import copy
import os
from tqdm import tqdm
import gc
from genome import *
from huffman import *

class LZ77():

    def __init__(self, l=7, w=20):

        # Size of the sliding window
        self.l = l
        # Size of the left window
        self.w = w
        # Initialize the dictionary
        self.source_word = ''
        self.new_symbol = []
        self.prev_dist = []
        self.prev_size = []

    def encode(self, sample):

        # Get buffer and fill it
        buffer = LZ_Buff(sample=sample,
                         size=self.l)
        # Track progress
        pbar = tqdm(total=len(sample))
        # Read all the sample:
        total_idx = 0
        while len(buffer) > 0:
            bf_end = len(buffer)
            # Search occurences
            offset = 0
            size = 0
            char = None
            tmp = None
            find = False
            t = 0
            while bf_end > 0 and t < self.w:
                tmp = buffer.get_string(end=bf_end)
                # Find occurences from the end
                find_idx = self.source_word.rfind(tmp)
                if find_idx != -1:
                    offset = buffer.start_idx - find_idx
                    size = len(tmp)
                    # Add the next char to tmp
                    tmp = buffer.get_string(end=bf_end+1)
                    find = True
                    break
                bf_end -= 1
                t += 1
            # If we have find an occurence
            if find:
                char = tmp[-1]
                # Append in arrays
                self.source_word = '{}{}'.format(self.source_word, tmp)
                self.new_symbol.append(char)
                self.prev_dist.append(offset)
                self.prev_size.append(size)
                pbar.update(size+1)
                # Update buffer:
                buffer.forward(len(tmp))

            # If occurence not find:
            else:
                self.source_word = '{}{}'.format(self.source_word, tmp)
                self.new_symbol.append(tmp[-1])
                self.prev_size.append(0)
                self.prev_dist.append(0)
                pbar.update(1)
                buffer.forward(1)

    def decode(self):

        decoded = ''

        # For each tuples of data in the dict
        for i in range(len(self.new_symbol)):
            # Get tuple:
            ll = self.new_symbol[i]
            dist = self.prev_dist[i]
            size = self.prev_size[i]

            # If we find an occurence:
            if dist != 0:
                start_index = len(decoded) - dist
                end_index = start_index + size
                bs = ''.join(decoded[start_index:end_index])
                decode = '{}{}'.format(bs, ll)
                #print(decode)
            else:
                decode = ll
                #print(ll)

            decoded = '{}{}'.format(decoded, decode)

        return decoded

    def get_encodage(self):

        symbol = []
        offset = []
        size = []
        print('Export encodage...')
        for i in tqdm(range(len(self.new_symbol))):
            # Add the symbol
            symbol.append(self.new_symbol[i])
            # Add binary offset encodage
            offset.append(str(bin(self.prev_dist[i])))
            # Add len of previous
            size.append(str(bin(self.prev_size[i])))

        return symbol, offset, size




class LZ_Buff():

    def __init__(self, sample, size):

        # Index of the buffer start
        self.start_idx = 0
        # Index of the buffer end
        self.end_idx = self.start_idx + size
        # The sample to read (array)
        self.sample = sample

        # Security:
        if self.end_idx > len(sample):
            self.end_idx = len(sample)

    def get_string(self, end=None):
        """
        return the content of the buffer in string format
        """
        if end is None:
            end = self.end_idx
        else:
            end = self.start_idx + end
        return ''.join(self.sample[self.start_idx:end])

    def forward(self, size):
        """
        Forward the buffer of size elements in the sequence
        """
        self.start_idx += size
        if self.start_idx > len(self.sample):
            self.start_idx = len(self.sample)

        self.end_idx += size
        if self.end_idx > len(self.sample):
            self.end_idx = len(self.sample)

    def get_seq(self, start, end):

        # Adapt index
        start = start + self.start_idx
        end = end + self.start_idx

        # Secu
        if start >= len(self.sample):
            return ''
        if end > len(self.sample):
            end = len(self.sample)

        return self.sample[start:end]


    def __len__(self):
        return self.end_idx - self.start_idx


def LZ_experiment_1():

    # Prepare the encoder
    test = LZ77(l=7, w=1000)
    # Get the string
    string = 'abracadabrad'
    # Encode it
    test.encode(string)
    # Get tuples:
    symbols, offset, size = test.get_encodage()

    for i in range(len(symbols)):
        print('({}, {}, {})'.format(str(offset[i]).replace('0b', ''), str(size[i]).replace('0b', ''), symbols[i]))


def LZ_experiment_2(l=7, w=10000):

    # Use LZ 77 with a buffer of size 7 and a window of size 1000
    test = LZ77(l=l, w=w)

    # Import sequence
    seq = import_genome(codon=False)

    # Encode teh sequence
    test.encode(seq)

    # Decode it
    decoded = test.decode()

    # Tcheck if no errors between encoded and decoded
    counter = 0
    for i in range(0, len(seq)):
        if seq[i] != decoded[i]:
            counter += 1

    print('Differences find in the file: ', counter)


    # Get triplets
    symbols, offset, size = test.get_encodage()

    # Get the size of encoded sec
    encoded_size = 0
    for i in range(len(symbols)):
        # print('{} - {} - {} - {} - {}'.format(symbols[i], offset[i], size[i], len(offset[i]), len(size[i])))
        encoded_size += 8 + len(offset[i]) + len(size[i]) - 4

    # Get original size:
    original_size = 8 * len(seq)
    compression_rate = encoded_size / original_size
    print('Original: {} bits, encoded: {} bits, compression rate: {}'.format(original_size,
                                                                             encoded_size,
                                                                             compression_rate))
    return original_size, encoded_size, compression_rate

def LZ_hoffman(l=7):

    # Get the genome
    gen = import_genome(codon=False)[0:100000]

    test = LZ77(l=l, w=100000)

    # Encode the sequence:
    test.encode(gen)

    # Get sequence of characters
    char_seq = test.new_symbol

    # Transform it into a string
    char_seq_str = ''.join(char_seq)

    # Compress it using huffman
    huff = Huffman(char_seq_str)
    huff.run_hoffman_code()
    # Get the string
    huff_encoded = huff.get_encoded_str()

    # Compare weight
    original_weight = len(gen) * 8

    # Get triplets
    symbols, offset, size = test.get_encodage()

    # Get the size of encoded sec
    encoded_size = 0
    for i in range(len(symbols)):
        # print('{} - {} - {} - {} - {}'.format(symbols[i], offset[i], size[i], len(offset[i]), len(size[i])))
        encoded_size += 8 + len(offset[i]) + len(size[i]) - 4

    # Size for huffman-LZ combination
    combi_size = encoded_size - 8 * len(symbols)
    for i in range(len(huff_encoded)):
        combi_size += len(huff_encoded[i])

    print('Original size: {}'.format(original_weight))
    print('LZ-encoded size: {}'.format(encoded_size))
    print('Huffman-LZ size: {}'.format(combi_size))

    # Get compressionr rates
    lz_rate = encoded_size/original_weight
    lz_huff_rate = combi_size/original_weight
    print('LZ rate: {}'.format(lz_rate))
    print('LZ-huff rate: {}'.format(lz_huff_rate))

    # Try hoffman alone:
    huff_alone = Huffman(gen)
    huff_alone.run_hoffman_code()
    # Get compressed elements
    huff_str = huff_alone.get_encoded_str()
    huff_size = 0
    for itm in huff_str:
        huff_size += len(itm)
    print('huff alone size: {}'.format(huff_size))
    print('huff alone compression rate: {}'.format(huff_size/original_weight))

    opt = [original_weight,
           encoded_size,
           huff_size,
           combi_size]
    return opt




















