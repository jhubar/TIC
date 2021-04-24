
from huffman import *
from chanelCoding import *


def run_part_2():
    sound_path = "suppl/sound.wav"
    coding = chanelCoding()

    # Q15 Give the plot of the signal.
    coding.plot_sound_signal()
    # Q16 Encode the sound signal using fixed-length binary code
    coding.encode_sound_signal()
    # Q17 SImulate the chanel on the binary sound signal
    """
    Probleme avec la binerazire du prof 
    """
    coding.simulate_and_decode()
    # 18 introduce redundancy
    coding.introduciton_of_redundancy()
    # 19
    """
    Il faut modifier le code de la 17 mais c'est la meme choses pas les
    même args
    """
    coding.simulate_and_decode()

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
