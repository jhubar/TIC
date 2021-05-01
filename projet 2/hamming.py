import config
import numpy as np
from utils import *

class hamming():
    def __init__(self):
        self.generator = config.GENERATOR_MATRIX
        self.parity_check = config.PARITY_CHECK
        self.values = [ i for i in range(len(self.parity_check[1]))]
        self.keys = [ np.array2string(self.parity_check[:, i]) for i in self.values]
        self.dict = dict(zip(self.keys, self.values) )
        self.no_error = np.array([0,0,0], dtype=int)
        self.encode_number = config.ENCODE_NUMBER
        self.decode_number = config.DECODE_NUMBER


    def encode(self,data):
        assert len(data) % self.encode_number == 0
        assert len(data) >= self.encode_number
        code = ""
        i = 0
        while i < len(data):
            code_bit_array = np.array(list(data[i : i + self.encode_number ]), dtype=int)
            encoded_message = (np.matmul(code_bit_array, self.generator) % 2)
            for code_bit in encoded_message:
                code += binarize(v = code_bit)
            i+=self.encode_number
        return code

    def decode(self,data):
        assert len(data) % self.decode_number == 0
        assert len(data) >= self.decode_number
        corrected = ""
        i = 0
        while i < len(data):
            hamming_code = np.array(list(data[i:i+self.decode_number ]), dtype=int)
            syndrome = (np.matmul(self.parity_check, hamming_code) % 2)
            if not (syndrome == self.no_error).all():
                incorrect_bit = self.dict[str(syndrome)]
                hamming_code[incorrect_bit] = (hamming_code[incorrect_bit] + 1) % 2
            for j in range(self.encode_number):
                corrected += binarize(v=hamming_code[j])
            i+=self.decode_number
        return corrected
