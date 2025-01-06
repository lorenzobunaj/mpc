from Crypto.Hash import SHA256

def xor2(a, b, l):
    return bytes([a[k] ^ b[k] for k in range(l)])

def xor(l, *args):
    if len(args) == 2:
        return xor2(args[0], args[1], l)
    else:
        return xor(l, xor2(args[0], args[1], l), *args[2:])

def PRG(seed, m):
    """
    Pseudorandom generator using SHA256.

    PRG : {0, 1}^K -> {0, 1}^m
    """
    output = b""
    while len(output) < m:
        seed = SHA256.new(seed).digest()
        output += seed
    return output[:m]

def CR_HASH(index, input_data, n):
    """
    Correlation robust hash function.

    CR_HASH: [m] x {0,1}^l -> {0,1}^n
    """
    
    if isinstance(input_data, tuple):
        input_data = b''.join(int.to_bytes(x, 1, byteorder='big') for x in input_data)  # Convert integers to bytes
    elif not isinstance(input_data, bytes):
        raise TypeError(f"Expected input_data to be bytes or tuple, got {type(input_data)}")
    
    hasher = SHA256.new()
    hasher.update(index.to_bytes(4, byteorder="big"))  # Represent index as 4 bytes
    hasher.update(input_data)
    return hasher.digest()[:n]

# example of log
KOT_choice_bits = [1, 0]
KOT_seeds = [b'\xee\t\x9c/\xe3k`1', b'\xed\x9c\xd3\xec\xd2\xb7\x0e*']
Ua = b'5\xbe*\xb7\x00G\x13i\xf9\xbc\xf7%\xcf\x03(\xa2\xdb\xce"A69\x1f\xada/R\x01\x81\x13QsQ\x1f\x009\xaf\xeb\xe3\x04\xd3\xae\xd5\xca\xd4\xbc\xe1\xceO$6\x88<\xcb\xc3\xff\xa8\x9e\x8d\x8b\x9d\xfdG\x902i[\xdb\x9e\x9a\x02\xc5\x8c\xff}\xd7!\xbb\x15i\xfe\x97$\x87\xad\xbf\x80T4\x0fGc\xcd$\xde\x8f\xb7\x8b\x874\x1a\x05\xb0\xbc'
Hab = [b'}\xbb\xc2\xbe\x06-\xfe8\x90S\x824\xe3-\x8eW%8\xff\x18\xd9\xedL,\x938\xbc\x81\xef\xc5:^', b'\x0fn\xfc/h\xbe\x96\x8c\xa7\xda>\x9a\\\xfbowV\xfd\x10\xec\xe5-_\x1b\xd7\x9a4\x05\xe0\xabsC', b'EV\xa0p\x0b\xf2L0\xcav\x04^\xc5\xe6S\xd1A\xc7\r\x87\xad\x1d\x19\xf4\xfcb-6f\x17\xe4\x18', b'q\x8b\r2Q\x9b053s\xbb\xf0\x12/3\xdb\xb3\xa8\xac\xe9n\x18\x8fjT1\x0e7\x1a\xcc5v']

'''
We know that r' = r | tau, where tau = 0 * 64, then we can find r' by finding r and appending tau to it

The consistency check provides and oracle to check wether a particular candidate rt is the input of the receiver

In fact, we can find G = [PRG(KOT_seeds[0], PRG(KOT_seeds[1])], where KOT_seeds are the chosen seeds that R sends to S.

We can then check if rt = r by computing t = Ua XOR G[0] XOR rt, and checking if

Hab[1 - KOT_choice_bits[0]][KOT_choice_bits[1]] = CR_HASH(t XOR G[1])

'''

m = 5
len_r = 64
tau = [0 for _ in range(len_r)]

def check_r(rt):
    rt = rt + tau

    G = [PRG(KOT_seeds[0], m + len_r), PRG(KOT_seeds[1], m + len_r)]

    if Hab[2 * (1 - KOT_choice_bits[0]) + KOT_choice_bits[1]] == CR_HASH(0, xor(m + len_r, Ua, rt, G[0], G[1]), m + len_r):
        print(rt)


def guess_r(rt):
    # print(rt)
    if len(rt) == 5:
        check_r(rt)
    else:
        guess_r(rt + [0])
        guess_r(rt + [1])

def solve():
    rt = []

    guess_r(rt)

if __name__ == "__main__":
    solve()