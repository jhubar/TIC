import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import os
import scipy.io
from scipy.io.wavfile import read
import numpy as np
import matplotlib.pyplot as plt
import random
import re
import time

from utils import *
from hamming import *

class chanelCoding():
    def __init__(self):
        self.rate, self.data = load_wav()
        self.sampleRate = None

        self.duration = len(self.data)/self.rate
        self.bin_data = ""
        self.channelized_data = ""

        self.num_of_bits = 8
        self.probability = 0.01
        self.decoded_data = []
        self.hamming_code = None
        self._hamming = hamming()
        # self.time = np.arange(0,self.data,1/self.rate).all()


    def binarize_data(self):
        for i in self.data:
            self.bin_data += binarize(i,nb = int(self.num_of_bits))
        return self.bin_data

    def encode_sound_signal(self):
        self.num_of_bits = np.log2(np.max(self.data) + 1)
        print("The number of bits to encode the sound signal is: "+ str(self.num_of_bits))
        self.binarize_data()

    def simulate_channel(self,input_data):
        self.channelized_data = ""
        for i in input_data:
            uniform = random.uniform(0, 1)
            if uniform <= self.probability:
                if i == '1':
                    self.channelized_data += '0'
                else:
                    self.channelized_data += '1'
            else:
                self.channelized_data += i



    def simulate_and_decode(self, input_data, name, decode = False):
        self.simulate_channel(input_data)
        if decode:
            self.channelized_data = self._hamming.decode(self.channelized_data)
        self.channelized_data = re.findall('.{1,8}', self.channelized_data)
        self.decoded_data = np.array([bin_to_dec(i) for i in self.channelized_data],dtype=np.uint8)
        self.plot_sound_signal(input_data = self.decoded_data, name = name, recorded_sound = True)



    def introduciton_of_redundancy(self):
        self.hamming_code = self._hamming.encode(self.bin_data)



    def plot_sound_signal(self,input_data , name, recorded_sound = False):

        plt.plot(input_data)
        plt.xlabel('Time [s]')
        plt.ylabel('Amplitude')
        plt.title("wav")
        plt.savefig("fig/"+name+".pdf")
        # plt.show()
        plt.close()
        if recorded_sound:
            save_wav("sound/"+name+".wav", self.rate, input_data)
