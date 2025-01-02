from protocol.wrapper import start_protocol, protocol
from oracles import KOT
from primitives import PRG, CR_HASH
from secrets import FLAG, SEED
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

SEED_LEN = 8
assert len(SEED) == SEED_LEN

def main():
    K = SEED_LEN * 8
    l = K
    n = 16
    m = 5

    encrypt_flag(FLAG, SEED)

    S, R = start_protocol(K, l, n, m, SEED)

    S_inputs = [(os.urandom(n // 8), os.urandom(n // 8)) for _ in range(m)]

    while True:
        R_inputs = input("Enter your choice bits: ")

        if not set(R_inputs).issubset({"1", "0"}) or len(R_inputs) != m:
            print("Bad input")
            break

        R_inputs = [int(b) for b in R_inputs]

        protocol(S, R, S_inputs, R_inputs, KOT, PRG, CR_HASH)

def encrypt_flag(flag, seed):
    key = (seed * 2).encode()

    print(key)
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    pt = pad(flag.encode(), AES.block_size)
    
    ct = cipher.encrypt(pt)
    
    print(ct)

if __name__ == "__main__":
    main()
