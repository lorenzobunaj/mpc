from protocol.sender import Sender
from protocol.receiver import Receiver

def start_protocol(K, r, l, n, m):
    S = Sender(K, r, l, m, n)
    R = Receiver(K, r, l, m, n)

    return [S, R]

def protocol(S, R, S_inputs, R_inputs, KOT, PRG, CR_HASH):
    # setup phase
    S.new_inputs(S_inputs)
    R.new_inputs(R_inputs)

    # initial OT phase
    KOT(R.KOT_send, S.KOT_send, S.KOT_receive)

    # extension phase 1
    S.receive_U(R.send_U(PRG))

    # consistency check
    check = S.consistency_check(R.consistency_check(PRG, CR_HASH), PRG, CR_HASH)
    if not check:
        return 0

    # extension phase 2
    R.receive_masked_strings(*S.send_masked_strings(PRG, CR_HASH), CR_HASH)

    # print(R.send_strings())

    return 1