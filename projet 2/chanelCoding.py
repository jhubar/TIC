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

from utils import *


class coding():
    def __init__(self):
        self.rate, self.data = load_wav()
        self.sampleRate = None
        
        self.duration = len(self.data)/self.rate
        self.bin_data = ""
        self.channelized_data = ""
        
        self.num_of_bits = 8
        self.probability = 0.01
        self.decoded_data = []
        
    
    def binarize_data(self):
        for i in self.data: 
            self.bin_data += binarize(i,int(self.num_of_bits))
        return str(self.bin_data)
    
    def encode_sound_signal(self):
        self.num_of_bits = np.log2(np.max(self.data) + 1)
        print("The number of bits to encode the sound signal is: "+ str(self.num_of_bits))
        self.binarize_data()
    
    def simulate_channel(self):
        for i in self.data:
            uniform = random.uniform(0, 1)
            if uniform <= self.probability:
                if i != 1: 
                    self.channelized_data = "1"
                else:
                    self.channelized_data = "0"
            else:
                self.channelized_data += str(i)


    def simulate_and_decode(self):
        self.simulate_channel()
        self.channelized_data = re.findall('.{1,8}', self.channelized_data)
        
        print(int(11271271,2))
        print(bin_to_dec(self.channelized_data[0]))
        
        
        self.decoded_data = np.array([bin_to_dec(val) for val in self.channelized_data],dtype=np.uint8)

    # def plot_sound_signal(self, data = None):
    #     if data is None:
    #         self.time = np.arange(0,self.data,1/self.rate) #time vector
    #         plt.plot(self.time,self.data)
    #     else:
    #         self.time = np.arange(0,data,1/self.rate) #time vector
    #         plt.plot(self.time,data)
    #     plt.xlabel('Time [s]')
    #     plt.ylabel('Amplitude')
    #     plt.title("wav")
    #     plt.savefig("fig/wav.pdf")
    #     plt.show()
    #     plt.close()