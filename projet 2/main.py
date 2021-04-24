
from huffman import *
from chanelCoding import *


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

    run_part_2()

    # P_S =  'BCAADDDCCACACAC'
    # huffman = Huffman(P_S)
    # huffman.run_hoffman_code()
    # huffman.print_huffman_code()


    # P_S = [ 8, 3, 3, 3, 3]
    # huffman = Huffman(P_S)
    # huffman.run_hoffman_code()
    # huffman.print_huffman_code()

    # P_S = [0.05, 0.10, 0.15, 0.15, 0.2, 0.35]
    # huffman = Huffman(P_S)
    # huffman.run_hoffman_code()
    # huffman.print_huffman_code()


    # coding.encode_sound_signal()
    # coding.simulate_and_decode()
    # coding.plot_sound_signal(coding.decoded_data)
