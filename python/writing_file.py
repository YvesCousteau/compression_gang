import pickle
# text_file = 'test.png'
# text_file = 'demo.txt'
text_file = 'hello_world.txt'
coding_file = 'demo_coding.dat'
decoding_file = 'demo_decoding.txt'
coding_file_shannon_fano = 'demo_shannon_fano_coding.dat'
decoding_file_shannon_fano = 'demo_shannon_fano_decoding.txt'
# ------------------------------ #
def writing_code_seq(seq):
    open(coding_file, 'w').close()
    f = open(coding_file, "wb")
    text_bytes = seq.encode('ascii')
    # pickle.dump(text_bytes,f)
    f.write(text_bytes)
# ------------------------------ #
def writing_code_seq_bit(seq):
    open(coding_file, 'w').close()
    f = open(coding_file, "wb")
    text_bytes = seq.encode('ascii')
    # pickle.dump(text_bytes,f)
    f.write(text_bytes)
# ------------------------------ #
def writing_decode_seq(seq):
    open(decoding_file, 'w').close()
    f = open(decoding_file, "a")
    f.write(seq)
    pass
# ------------------------------ #
def writing_code_seq_shannon_fano(seq):
    open(coding_file_shannon_fano, 'w').close()
    f = open(coding_file_shannon_fano, "wb")
    text_bytes = seq.encode('ascii')
    # pickle.dump(text_bytes,f)
    f.write(text_bytes)
# ------------------------------ #
def writing_decode_seq_shannon_fano(seq):
    open(decoding_file_shannon_fano, 'w').close()
    f = open(decoding_file_shannon_fano, "a")
    f.write(seq)
    pass
# ------------------------------ #
def cmp():
    f = open(text_file, "r")
    temp = ''.join(format(ord(x),'b') for x in f.read())
    open('demo_without_huffman.dat', 'w').close()
    f = open("demo_without_huffman.dat", "wb")
    f.write(temp.encode('ascii'))
    pass
