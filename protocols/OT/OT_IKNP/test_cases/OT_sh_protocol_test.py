from ..OT_SH_extension.protocol.wrapper import OT_sh_protocol
from ..OT_SH_extension.primitives import PRG, CR_HASH
from ..OT_SH_extension.oracles import KOT
import os

def protocol_test():
    K = 64
    l = K
    n = 16
    m = 5

    for i in range(10):
        S_inputs = [(os.urandom(n // 8), os.urandom(n // 8)) for _ in range(m)]
        R_inputs = [int.from_bytes(os.urandom(1), byteorder="big") % 2 for _ in range(m)]

        expected_results = [S_inputs[i][R_inputs[i]] for i in range(m)]
        real_results = OT_sh_protocol(K, l, n, m, S_inputs, R_inputs, KOT, PRG, CR_HASH)

        print(f"Test case {i+1}: " + ("" if real_results == expected_results else "not ") + "passed")

if __name__ == "__main__":
    protocol_test()