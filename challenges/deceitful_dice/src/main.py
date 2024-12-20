import os
from oracles import KOT
from primitives import PRG, PRG_more_random, CR_HASH
from protocol.wrapper import OT_sh_protocol
from secrets import FLAG

LEN_FLAG = 28

assert len(FLAG) == LEN_FLAG

def main():
    K = 64
    l = K
    n = 16
    m = 8 * LEN_FLAG

    S_inputs = [(os.urandom(n // 8), os.urandom(n // 8)) for _ in range(m)]
    R_inputs = [(ord(c) >> i) & 1 for i in reversed(range(8)) for c in FLAG]

    with open("output.txt", "a") as file:
        file.write("\n########################################\n")

    OT_sh_protocol(K, l, n, m, S_inputs, R_inputs, KOT, PRG, PRG_more_random, CR_HASH)

if __name__ == "__main__":
    main()
