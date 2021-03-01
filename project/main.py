"""
ELEN060-2
2020 - 2021
Information and coding theory
Project 1 - Information measures
François LIEVENS - 20103816
Julien HUBAR - 10152485
"""
from question_1_to_5 import *
from question_6_to_11 import *
from question_12_to_17 import *
import numpy as np





if __name__ == "__main__":
    dist_y = [1/2,1/4,1/8,1/8]
    dist_x = [1/4,1/4,1/4,1/4]

    dist_x_1 = [1/8,1/16,1/32,1/32]
    dist_x_2 = [1/16,1/8,1/32,1/32]
    dist_x_3 = [1/32,1/32,1/16,0]
    dist_x_4 = [1/32,1/32,1/16,0]

    dist_x_y = np.matrix(
                 [[1/8 ,1/16,1/16,1/4]
                ,[1/16,1/8 ,1/16,0]
                ,[1/32,1/32,1/16,0]
                ,[1/32,1/32,1/16,0]])


    # print(joint_entropy(dist_x_y))

    # print(mutual_information(dist_x_y, dist_x,dist_y))

    # h1 = entropy(dist_x_y[0][0])
    # h2 = entropy(dist_x_2)
    # h3 = entropy(dist_x_3)
    # h4 = entropy(dist_x_4)
    # print(h1)
    # print(h2)
    # print(h3)
    # print(h4)
    # print(h1 + h2 + h3 + h4 )
    # print( 27/8 )
    entropy_of_mediacal_data()
