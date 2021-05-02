from math import ceil, log2

class LZ():
    def __init__(self):
        self.dictionnary = {
            'λ': {
                'c': 0,
                'c_bin': '{0:b}'.format(0),
                'l2': "-",
                'code': "",
            }
        }

        self.DEBUG = False

    def encode(self, sentence):

        output = ""

        keys_ = sorted(self.dictionnary, key=len)[::-1]

        index = 0
        while index < len(sentence):
            print("\r",
                  f"Encoding for online LZ {index}/{len(sentence)}       {round(index / len(sentence) * 100, 2)}%",
                  end="")
            for k in keys_:
                if sentence[index: index+len(k)] == k:
                    index += len(k)
                    output += self.dictionnary[k]["code"]

        return output

    def create_dict(self, sentence):

        s = 0
        while s <= len(sentence):

            print("\r",
                  f"Creating dictionnary for online LZ {s}/{len(sentence)}       {round(s/len(sentence)*100, 2)}%",
                  end="")

            if self.DEBUG:
                print("Remaining sentence: {}".format(sentence[s:]))
            len_sa = self.analyse(sentence, s)
            s += len_sa

    def analyse(self, sentence, s):

        counter = 1
        for i in range(s + 1, len(sentence)+1):

            character = sentence[s:i]

            if self.DEBUG:
                print(character)
                print("Is not in keys: {}".format(character not in self.dictionnary.keys()))

            if character not in self.dictionnary.keys():
                self.dictionnary[character] = self.add_character(character)
                break

            counter += 1

        return counter

    def add_character(self, character):

        dct = {}

        all_c = []
        for k in self.dictionnary.keys():
            all_c.append(self.dictionnary[k]['c'])

        c = max(all_c) + 1
        dct['c'] = c
        dct['c_bin'] = '{0:b}'.format(c)
        dct['l2'] = ceil(log2(c))
        dct['code'] = self.get_prefix_cbin(ceil(log2(c)), character[:-1]) + str(character[-1])

        return dct

    def get_prefix_cbin(self, size, prefix):

        if prefix == "":
            return "0" * size

        shortened_p = self.dictionnary[prefix]['c_bin'][::-1][:size][::-1]

        if len(shortened_p) < size:
            shortened_p = (size - len(shortened_p)) * "0" + shortened_p

        return shortened_p

    def print_dict(self):

        for k in self.dictionnary.keys():
            print('\033[93m' + k + "\033[0m")
            for l in self.dictionnary[k].keys():
                print("    " + '\033[94m' + l + "\033[0m" + ":  " + str(self.dictionnary[k][l]))
