"""
ELEN060-2
2020 - 2021
Information and coding theory
Project 1 - Information measures
François LIEVENS - 20103816
Julien HUBAR - 10152485
Implementation of question 12 to 17
"""
import numpy as np
from question_1_to_5 import *
class Board():

    def __init__(self):
        self.R = 0
        self.C = 0
        self.M = 0

    def set_R(self,r):
        self.R = r
    def set_C(self,c):
        self.C = c
    def set_M(self,m):
        self.M = m/(self.R*self.C)

    def entropy_of_board(self):
        nums = np.random.choice([1, 0], size=10, p=[self.M, 1-self.M])
        print(entropy(nums))
