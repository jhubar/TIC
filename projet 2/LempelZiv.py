import numpy as np
import copy
import os

class LZ77():

    def __init__(self, l=3):

        # Size of the sliding window
        self.l = l
        # Initialize the dictionary
        self.source_word_historique = ['']
        self.source_word = ''
        self.new_symbol = []
        self.prev_dist = []
        self.prev_size = []

    def encode(self, sample):

        # Get buffer and fill it
        buffer = LZ_Buff(sample=sample,
                         size=self.l)

        # Read all the sample:
        while len(buffer) > 0:

            bf_end = len(buffer)
            # Search occurences
            offset = 0
            size = 0
            char = None
            tmp = None
            find = False
            while bf_end > 0:
                tmp = buffer.get_string(end=bf_end)
                print(tmp)
                # Find occurences from the end
                find_idx = self.source_word.rfind(tmp)
                if find_idx != -1:
                    print('FIND: tmp: {}, find_idx: {}'.format(tmp, find_idx))
                    offset = buffer.start_idx - find_idx
                    size = len(tmp)
                    # Add the next char to tmp
                    tmp = buffer.get_string(end=bf_end+1)
                    find = True
                    break
                bf_end -= 1
            # If we have find an occurence
            if find:
                char = tmp[-1]
                # Append in arrays
                self.source_word = '{}{}'.format(self.source_word, tmp)
                self.source_word_historique.append(copy.deepcopy(self.source_word))
                self.new_symbol.append(char)
                self.prev_dist.append(offset)
                self.prev_size.append(size)
                # Update buffer:
                buffer.forward(len(tmp))

            # If occurence not find:
            else:
                self.source_word = '{}{}'.format(self.source_word, tmp)
                self.source_word_historique.append(copy.deepcopy(self.source_word))
                self.new_symbol.append(tmp[-1])
                self.prev_size.append(0)
                self.prev_dist.append(0)
                buffer.forward(1)














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












