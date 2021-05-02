import config
from collections import Counter
import matplotlib.pyplot as plt
import random
import numpy as np
from huffman import *

def import_genome(codon : True, size = 0):
    with open('suppl/genome.txt') as f:
        lines = f.readlines()


    gen = []
    if size is not None:
        for i in range(len(lines)):
            if lines[i][-1] == '\n':
                lines[i] =  lines[i][:-1]
            gen.append(lines[i])

        gen = ''.join(gen)


        if codon == True:
            tmp = []
            genome = []
            if size == 0:
                for i in range(len(gen)):
                    tmp.append(gen[i])
                    if (i+1)%config.SIZE_CODON == 0:
                        tmp = ''.join(tmp)
                        genome.append(tmp)
                        tmp = []
                return genome
            else:
                # s=gen
                # gen = ''.join(random.sample(s,len(s)))

                for i in range(size):
                    tmp.append(gen[i])
                    if (i+1)%config.SIZE_CODON == 0:
                        tmp = ''.join(tmp)
                        genome.append(tmp)
                        tmp = []
                return genome
        else:
            return gen




def count_occ(data):
    return Counter(data)


def barplot_dict(dict):
    plt.bar(range(len(dict)), list(dict.values()), align='center')
    plt.xticks(range(len(dict)), list(dict.keys()), rotation=90, ha='right')

    plt.savefig('fig/dist_gen.pdf')
    plt.show()
    plt.close()

def code_length(dist, code_length):

    dist_items = dist.items()

    code_length_items = code_length.items()


    sorted_dist_items = sorted(dist_items)
    sorted_code_length_items = sorted(code_length_items)
    code_length = []
    avg_code_length = []
    sum_dist_item = 0
    for i in range(len(dist)):
        sum_dist_item+= sorted_dist_items[i][1]
    total_size_gen = sum_dist_item*3*7

    for i in range(len(dist)):
        code_length.append((sorted_dist_items[i][1])*len(sorted_code_length_items[i][1]))
        avg_code_length.append((sorted_dist_items[i][1]/sum_dist_item)*len(sorted_code_length_items[i][1]))

    print(' Code Length in bits ')
    print('--------------------------')
    print(str(sum(code_length))+" bits")
    print('--------------------------')
    print(str(sum(avg_code_length))+" bits")

    return sum(avg_code_length)

def plot_empirical_average_length(values,x_value):

    plt.plot(values)
    # plt.xticks(range(len(values)), rotation=90, ha='right')
    plt.xlabel("Input genome lengths")
    plt.ylabel("Empirical average length")
    plt.show()
    plt.close()


def empirical_average_length(total_length):
    len_code_array = []
    len_code_array_size = []
    i= config.size_increasing

    while i < total_length:

        gen = import_genome(codon = True, size = 0)
        idx_array = np.arange(len(gen))
        np.random.shuffle(idx_array)
        idx_array = idx_array.tolist()

        new_gen = []
        for itm in idx_array:
            new_gen.append(gen[itm])

        gen = new_gen
        huffman = Huffman(gen[0:i])
        huffman.run_hoffman_code()
        dist_gen = count_occ(gen[0:i])
        len_code_array.append(code_length(dist = dist_gen, code_length = huffman.huffman_code))
        len_code_array_size.append(str(i))
        i+= config.size_increasing
    plot_empirical_average_length(len_code_array,len_code_array_size)
