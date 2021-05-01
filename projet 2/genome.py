from collections import Counter
import matplotlib.pyplot as plt

def import_genome():
    with open('suppl/genome.txt') as f:
        lines = f.readlines()


    gen = []
    print(lines[0])
    for i in range(len(lines)):
        if lines[i][-1] == '\n':
            lines[i] =  lines[i][:-1]
        gen.append(lines[i])

    gen = ''.join(gen)

    tmp = []
    genome = []
    for i in range(len(gen)):
        tmp.append(gen[i])
        if (i+1)%3 == 0:
            tmp = ''.join(tmp)
            genome.append(tmp)
            tmp = []

    return genome


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
    sum_dist_item = 0
    for i in range(len(dist)):
        sum_dist_item+= sorted_dist_items[i][1]

    for i in range(len(dist)):
        code_length.append((sorted_dist_items[i][1]/sum_dist_item)*len(sorted_code_length_items[i][1]))

    print(' Code Length in bits ')
    print('--------------------------')
    print(str(sum(code_length))+" bits")
