
from LempelZiv import *


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

print(decoded)

