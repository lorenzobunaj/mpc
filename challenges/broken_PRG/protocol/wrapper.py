from protocol.sender import Sender
from protocol.receiver import Receiver

def OT_sh_protocol(K, l, n, m, S_inputs, R_inputs, KOT, PRG, CR_HASH):
    S = Sender(K, l, m, n)
    R = Receiver(K, l, m, n)

    S.new_inputs(S_inputs)
    R.new_inputs(R_inputs)

    KOT(R.KOT_send, S.KOT_send, S.KOT_receive)

    S.receive_u(R.send_u(PRG), PRG)

    R.receive_masked_messages(*S.send_masked_messages(CR_HASH), CR_HASH)

    return R.send_last_results()