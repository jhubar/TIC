from LZ77 import *
from genome import *


if __name__ == "__main__":

    gen = import_genome(codon = False)

    test = LZ77(l=7, w=20)
    test.encode(gen)

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