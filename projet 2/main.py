
from huffman import *
from chanelCoding import *


if __name__ == "__main__":


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

    sound_path = "suppl/sound.wav"
    
    coding = coding()
    
    # coding.plot_sound_signal()
    coding.encode_sound_signal()
    coding.simulate_and_decode()
    # coding.plot_sound_signal(coding.decoded_data)

