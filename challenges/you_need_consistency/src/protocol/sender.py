from utils import xor
import os

class Sender:
    def __init__(self, K, l, m, n, FLAG):
        self.K = K  # security parameter
        self.l = l # number of base OT in the initial phase
        self.m = m  # number of base OT in the extension phase
        self.n = n  # lenght of each message

        self.S_inputs = []

        self.KOT_s = [int(bit) for char in FLAG for bit in f"{ord(char):08b}"]
        # self.KOT_s = [int.from_bytes(os.urandom(1), byteorder="big") % 2 for _ in range(l)]  # random vector s
        self.kc = None
        self.Q = None

    def new_inputs(self, S_inputs):
        self.S_inputs = []
        for i in range(self.m):
            self.S_inputs.append(S_inputs[i])

    def KOT_send(self):
        return self.KOT_s
    
    def KOT_receive(self, kc):
        self.kc = kc

    def receive_u(self, u, PRG):
        """
        Receive u and use it to compute Q
        """

        Qt = [
            bytes(
                [((self.KOT_s[i] * u[i][j]) ^ PRG(self.kc[i], self.m)[j])
                for j in range(self.m)]
            )
            for i in range(self.l)
        ]

        self.Q = list(zip(*Qt))  # transpose of Qt (l x m -> m x l)

        for row in self.Q:
            print(bytes(row))

        return [bytes(row) for row in self.Q]

    def send_masked_messages(self, CR_HASH):
        """
        Mask the messages (x0_j, x1_j) based on Q.
        """

        y0 = []
        y1 = []

        for j in range(self.m):
            qj = self.Q[j]
            x0_j, x1_j = self.S_inputs[j]

            h0 = CR_HASH(j, qj, self.n // 8)
            h1 = CR_HASH(j, xor(qj, self.KOT_s, self.l), self.n // 8)

            y0.append(xor(x0_j, h0, self.n // 8))
            y1.append(xor(x1_j, h1, self.n // 8))
        
        return [y0, y1]