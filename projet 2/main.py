
from huffman import *
from chanelCoding import *
from LZ77 import *
from Lempel_Ziv import *
from genome import *
import matplotlib.pyplot as plt



def run_part_1():

    # test hoffman algo
    P_S =  'BCAADDDCCACACAC'
    huffman = Huffman(P_S)
    huffman.run_hoffman_code()
    huffman.print_huffman_code()

    # Q1
    P_S = [0.05, 0.10, 0.15, 0.15, 0.2, 0.35]
    huffman = Huffman(P_S)
    huffman.run_hoffman_code()
    huffman.print_huffman_code()

    # Q2
    lempel_ziv = Lempel_ziv(config.SEQUENCE_BIT)
    lempel_ziv.create_sub_sequence()
    lempel_ziv.code_representation()
    print("--------------------------------------")
    print(lempel_ziv.binary_encoded)
    print((list(lempel_ziv.keys)))
    print(lempel_ziv.binary_encoded)
    print("--------------------------------------")



    # Q4
    LZ_experiment_1()

    # Q5,Q6
    # REMOVE [0:1000] for compute all genome
    gen = import_genome(codon = True, size = 0)[0:1000]
    total_length = len(gen)
    #
    huffman = Huffman(gen)
    huffman.run_hoffman_code()
    huffman.print_huffman_code()
    dist_gen = count_occ(gen)
    barplot_dict(dist_gen)
    len_code = code_length(dist = dist_gen, code_length = huffman.huffman_code)
    # Q7
    empirical_average_length(total_length)
    i = 1
    array_compression = []
    while i <= 8:
        config.SIZE_CODON = i
        gen = import_genome(codon = True, size = 0)[0:100000]
        total_length = len(gen)
        huffman = Huffman(gen)
        huffman.run_hoffman_code()
        # huffman.print_huffman_code()
        dist_gen = count_occ(gen)
        # barplot_dict(dist_gen)
        array_compression.append(code_length(dist = dist_gen, code_length = huffman.huffman_code, flag = True))
        i+=1
    print(array_compression)
    plt.plot(np.arange(1,9),array_compression)
    plt.savefig('fig/evolution_of_comression.pdf')
    plt.xlabel('size of custom codon')
    plt.ylabel('Compression rate')
    plt.show()
    plt.close()


    # Q9

    gen = import_genome(codon = False, size = 0)
    gen = binary_genome(input = gen)
    lempel_ziv = Lempel_ziv(gen)
    lempel_ziv.create_sub_sequence()
    lempel_ziv = lempel_ziv.code_representation()
    cpt = 0
    for itm in lempel_ziv:
        cpt+= len(itm)-2
    print(cpt)
    print(len(gen))
    print("----------------------")
    print("compressions rate:  "+str(cpt/len(gen)))
    print("----------------------")


    #Q10
    LZ_experiment_2()

    # Q13
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



def run_part_2():
    sound_path = "suppl/sound.wav"
    coding = chanelCoding()
    # Q15 Give the plot of the signal.
    coding.plot_sound_signal(input_data = coding.data, name = "original")
    # Q16 Encode the sound signal using fixed-length binary code
    coding.encode_sound_signal()
    # Q17 SImulate the chanel on the binary sound signal
    coding.simulate_and_decode(input_data = coding.bin_data, name="channelized")
    # 18 introduce redundancy
    coding.introduciton_of_redundancy()
    # 19
    coding.simulate_and_decode(input_data = coding.hamming_code, name="hamming", decode = True)

if __name__ == "__main__":
    run_part_1()
    run_part_2()
