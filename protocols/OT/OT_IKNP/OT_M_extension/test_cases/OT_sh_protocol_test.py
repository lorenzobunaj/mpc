from protocols.OT.OT_IKNP.OT_M_extension.protocol.sender import Sender
from protocols.OT.OT_IKNP.OT_M_extension.protocol.receiver import Receiver
from oracles import KOT
from primitives import PRG, CR_HASH
import os

def OT_sh_protocol(K, l, n, m, S_inputs, R_inputs, KOT, PRG, CR_HASH):
    sender = Sender(K, l, m, n)
    receiver = Receiver(K, l, m, n)

    sender.new_inputs(S_inputs)
    receiver.new_inputs(R_inputs)

    KOT(receiver.KOT_send, sender.KOT_send, sender.KOT_receive)

    sender.receive_u(receiver.send_u(PRG), PRG)

    receiver.receive_masked_messages(*sender.send_masked_messages(CR_HASH), CR_HASH)

    return receiver.send_last_results()

def OT_sh_protocol_test():
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
    OT_sh_protocol_test()