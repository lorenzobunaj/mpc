from protocol.sender import Sender
from protocol.receiver import Receiver

def OT_m_protocol(K, r, l, n, m, S_inputs, R_inputs, KOT, PRG, CR_HASH):
    # setup phase
    S = Sender(K, r, l, m, n)
    R = Receiver(K, r, l, m, n)
    S.new_inputs(S_inputs)
    R.new_inputs(R_inputs)

    # initial OT phase
    KOT(R.KOT_send, S.KOT_send, S.KOT_receive)

    # extension phase 1
    S.receive_U(R.send_U(PRG), PRG)

    # consistency check
    check = S.consistency_check(R.consistency_check(PRG, CR_HASH), PRG, CR_HASH)
    if not check:
        return 0

    # extension phase 2
    R.receive_masked_strings(*S.send_masked_strings(PRG, CR_HASH), CR_HASH)

    # print(R.send_strings())

    return 1