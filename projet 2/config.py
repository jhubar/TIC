import numpy as np


GENERATOR_MATRIX = np.array([[1, 0, 0, 0, 1, 0, 1],
                             [0, 1, 0, 0, 1, 1, 0],
                             [0, 0, 1, 0, 1, 1, 1],
                             [0, 0, 0, 1, 0, 1, 1]])


PARITY_CHECK = np.array([[1, 1, 1, 0, 1, 0, 0],
                         [0, 1, 1, 1, 0, 1, 0],
                         [1, 0, 1, 1, 0, 0, 1]])


DECODE_NUMBER = 7
ENCODE_NUMBER = 4

SEQUENCE = 'AABABBBABAABABBBABBABB'
SEQUENCE_BIT = '1011010100010'
SIZE_CODON = 3
size_increasing = 2000
