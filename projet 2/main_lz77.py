from LZ77 import *
from genome import *
from lz_andreas import *


if __name__ == "__main__":

    # First exo
    LZ_experiment_1()

    # Second experiment
    gen = import_genome(codon=False)
    #gen = gen[0:10]

    # Get it on the genome
    original_size, encoded_size, compression_rate = LZ_experiment_2(l=7, w=10000)
    exit(0)


    lz_a = LZ()
    lz_a.create_dict(gen)
    lz_encoded = lz_a.encode(gen)
    print(lz_encoded)
    lz_a.print_dict()

    weight = 0
    for key in lz_a.dictionnary.keys():
        weight += len(key) * 7
        #weight += len(str(bin(lz_a.dictionnary[key]['c']))) - 2
        weight += len(lz_a.dictionnary[key]['c_bin'])
        try:
            weight += len(str(bin(lz_a.dictionnary[key]['l2'])))
        except:
            print('nope')
        weight += len(lz_a.dictionnary[key]['code'])

    init = len(gen) * 8

    print('init size: {}'.format(init))
    print('compressed: {}'.format(weight))
    rate = weight/init
    print('compression rate: {}'.format(rate))



    # Third experiment


    original_size = []
    lz_size = []
    huff_size = []
    combi_size = []
    lz_rate = []
    combi_rate = []
    lz_rate = []
    huff_rate = []

    for i in range(1, 20):
        print("ITER {} / {}".format(i, 20))
        orig, lz, huff, comb, = LZ_hoffman(l=i)

        original_size.append(orig)
        lz_size.append(lz)
        huff_size.append(huff)
        lz_rate.append(lz/orig)
        huff_rate.append(huff/orig)
        combi_rate.append(comb/orig)

    x = range(1, 20)

    plt.plot(x, lz_rate, c='blue', label='LZ-77')
    plt.plot(x, huff_rate, c='green', label='Huffman')
    plt.plot(x, combi_rate, c='red', label='Combination')
    plt.title('Compression rate')
    plt.xlabel('size of the window')
    plt.ylabel('Compression rate')
    plt.show()
    plt.close()






