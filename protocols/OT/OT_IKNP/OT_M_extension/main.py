from protocols.OT.OT_IKNP.OT_M_extension.protocol.sender import Sender
from protocols.OT.OT_IKNP.OT_M_extension.protocol.receiver import Receiver
from oracles import KOT
from primitives import PRG, CR_HASH
from protocol.wrapper import OT_sh_protocol
import os

def main():
    K = 64
    l = K
    n = 16
    m = 5

    S_inputs = [(os.urandom(n // 8), os.urandom(n // 8)) for _ in range(m)]
    R_inputs = [int.from_bytes(os.urandom(1), byteorder="big") % 2 for _ in range(m)]

    OT_sh_protocol(K, l, n, m, S_inputs, R_inputs, KOT, PRG, CR_HASH)

if __name__ == "__main__":
    main()
