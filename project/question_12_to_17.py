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

    def __init__(self, r = 0, c = 0, m=0 ):
        self._r = r
        self._c = c
        self._size = self._r * self._c
        self._m = m/self._size
        self._grid = [[]]

    def entropy_of_each_field_in_foard(self):
        den = self._size
        num = self._size
        mine = self._m*self._size
        print(mine)
        nb_bits = []
        for i in range(0,self._r):
            for j in range(0,self._c):
                if den == 0 or mine == 0 or num == 0:
                    break
                elif self._grid[i][j] == 0:
                    num -= 1
                    if num == 0:
                        break
                    print(str(num)+"/"+str(den)+" = "+str( -np.log2(num/den)))
                    nb_bits.append(-np.log2(num/den))
                    den -= 1
                else:
                    print(str(mine)+"/"+str(den)+" = "+str( -np.log2(mine/den)))
                    nb_bits.append(-np.log2(mine/den))
                    mine -=1
                    num -= 1
                    den -= 1
        print("The number of bits is equal to: "+str(np.sum(nb_bits)) )



    def entropy_of_board(self, nums = None ):

        if nums == None:
            nums = np.random.choice([1, 0], size=self._size, p=[self._m, 1-self._m])
        self._grid = np.reshape(nums,(self._r,self._c))
        print(self._grid)






if __name__ == "__main__":
    # grid = np.reshape([0,1,2,3,2,1,2,0,0,0,1,0,0,0,0],(5,2))
    board = Board(4,4,2)
    board.entropy_of_board(nums = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    #
    board.entropy_of_each_field_in_foard()
