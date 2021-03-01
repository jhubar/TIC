"""
ELEN060-2
2020 - 2021
Information and coding theory
Project 1 - Information measures
François LIEVENS - 20103816
Julien HUBAR - 10152485
Implementation of question 1 to 5
"""
import numpy as np
import pandas as pd
import math

def entropy(dist):
    """
    Quesiton 1: compute the entropy of a random varible
    """
    h=0
    for p in dist:
        r= p/sum(dist)
        if r!=0:
            h+= -r*(np.log(r))
    return h/np.log(2)


def joint_entropy(dist_x_y):
    """
    Quesiton 2: compute the joint entropy of a two discrete random varibles
    """
    h = 0
    for p_y in range(dist_x_y.shape[0]):
        for p_x in range(dist_x_y.shape[1]):
            r = dist_x_y[p_y,p_x]
            if r != 0:
                h += -r * np.log(r)
    return h/np.log(2)

def conditional_entropy(dist_x_y, cond_d):
    """
    Quesiton 3: compute the conditional entropy of a two discrete random varibles
    """
    h = 0
    for p_y in range(dist_x_y.shape[0]):
        for p_x in range(dist_x_y.shape[1]):
            r = dist_x_y[p_y,p_x]
            cond = cond_d[p_y]
            if r != 0 and cond != 0:
                h += -r * np.log(r/cond)
    return h/np.log(2)

def mutual_information(dist_x_y, dist_x, dist_y):
    """
    Quesiton 4: compute the mutual infomation of a two discrete random varibles


    """
    return entropy(dist_x) + entropy(dist_y) - joint_entropy(dist_x_y)


def cond_joint_entropy(dist_x_y_z, cond_d):
    """
    Quesiton 5: compute the conditional joint entropy of a two discrete random
                varibles knowing an another one
    """
    h = 0
    for p_y in dist_x_y_z.shape[0]:
        for p_x in dist_x_y_z.shape[1]:
            for p_z in dist_x_y_z.shape[2]:
                r = dist_x_y_z[p_y,p_x,p_z]
                cond = cond_d[p_z]
                if r != 0 and cond != 0:
                    h += -r * np.log(r/cond)
    return h/np.log(2)

def cond_mutual_entropy(dist_x, dist_y_z, dist_x_y_Z , cond_d):
    """
    Quesiton 5: compute the mutual infomation of a two discrete random varibles
                knowing an another one     I(X,Y|Z) = H(x) + H(Y|Z) - H(X,Y|Z)
    """
    return (entropy(x)
        + conditional_entropy(dist_x_y = dist_y_z, cond_d = cond_d )
        - cond_joint_entropy(dist_x_y_z, cond_d))
