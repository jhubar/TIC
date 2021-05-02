
from huffman import *
from chanelCoding import *
from LZ77 import *
from Lempel_Zip import *
from genome import *


def run_part_1():
    # test hoffman algo
    # P_S =  'BCAADDDCCACACAC'
    # huffman = Huffman(P_S)
    # huffman.run_hoffman_code()
    # huffman.print_huffman_code()
    #
    # # Q1
    # P_S = [0.05, 0.10, 0.15, 0.15, 0.2, 0.35]
    # huffman = Huffman(P_S)
    # huffman.run_hoffman_code()
    # huffman.print_huffman_code()

    # Q2

    lempel_zip = Lempel_zip(config.SEQUENCE)
    lempel_zip.create_sub_sequence()
    lempel_zip.code_representation()
    lempel_zip.binary_adddress()

    #
    # Q4
    """
    test = LZ77(l=3)

    sample = 'BASILE BAVE DANS SON BAVOIR'

    test.encode(sample)

    for i in range(0, len(test.prev_size)):
        print('{} - {} - {} - {}'.format(test.source_word_historique[i],
                                         test.new_symbol[i],
                                         test.prev_dist[i],
                                         test.prev_size[i]))

    print('TEST: =============')
    for i in range(0, len(test.new_symbol)):
        print('{} - {} - {}'.format(test.new_symbol[i],
                                    test.prev_dist[i],
                                    test.prev_size[i]))

    print('DECODING: ======================')

    decoded = test.decode()
    """
    #
    # print(decoded)
    # Q5,Q6
    # gen = import_genome(codon = False)
    # print(gen)
    # huffman = Huffman(gen)
    # huffman.run_hoffman_code()
    # huffman.print_huffman_code()

    # dist_gen = count_occ(gen)
    #
    # # barplot_dict(dist_gen)
    # code_length(dist = dist_gen, code_length = huffman.huffman_code)
    # # Q7
    # huffman_sort_encoded = huffman.huffman_encoded()
    # print(huffman_sort_encoded)
    # plot_empirical_average_length(huffman_sort_encoded)

    # Q9

    gen = import_genome(codon = False)
    lempel_zip = Lempel_zip(gen)
    lempel_zip.create_sub_sequence()
    lempel_zip.code_representation()
    lempel_zip.binary_adddress()

    # Get arrays
    numerical_rep = lempel_zip.numerical_representation
    # Compute weight
    weight = 0
    for itm in numerical_rep:
        weight += len(itm) - 2

    print('Lempel Ziv compression: ')
    print('Original weight: {}'.format(len(gen)*7))
    print('Compressed weight: {}'.format(weight))
    print('Compression rate: {}'.format(weight/(len(gen)*7)))
    # Q10
    # test = LZ77(l=3)
    # test.encode(gen)
    #
    # for i in range(0, len(test.prev_size)):
    #     print('{} - {} - {} - {}'.format(test.source_word_historique[i],
    #                                      test.new_symbol[i],
    #                                      test.prev_dist[i],
    #                                      test.prev_size[i]))
    #
    # print('TEST: =============')
    # for i in range(0, len(test.new_symbol)):
    #     print('{} - {} - {}'.format(test.new_symbol[i],
    #                                 test.prev_dist[i],
    #                                 test.prev_size[i]))
    #
    # print('DECODING: ======================')
    #
    # decoded = test.decode()












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
    # run_part_2()
