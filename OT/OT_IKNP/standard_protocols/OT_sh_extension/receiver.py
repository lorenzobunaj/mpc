from utils import xor
import os

class Receiver:
    def __init__(self, K, l, m, n):
        self.K = K  # security parameter
        self.l = l # number of base OT in the initial phase
        self.m = m  # number of base OT in the extension phase
        self.n = n  # lenght of each message

        self.R_inputs = []

        self.K_seeds = [(os.urandom(K // 8), os.urandom(K // 8)) for _ in range(l)]  # seeds for K-OT
        self.T = None

        self.last_results = None

    def new_inputs(self, R_inputs):
        for i in range(self.m):
            self.R_inputs.append(R_inputs[i])

    def KOT_send(self):
        return self.K_seeds

    def send_u(self, PRG):
        """
        Compute u and send it to the sender.
        """

        Tt = [PRG(self.K_seeds[i][0], self.m) for i in range(self.l)]
        u = [xor(xor(Tt[i], PRG(self.K_seeds[i][1], self.m), self.m), self.R_inputs, self.m) for i in range(self.l)]

        self.T = list(zip(*Tt))

        # print(self.T)
        
        return u

    def receive_masked_messages(self, y0, y1, CR_HASH):
        """
        Receive masked messages and reconstruct the selected messages.
        """

        results = []
        for j in range(self.m):
            tj = self.T[j]
            h_tj = CR_HASH(j, tj, self.n // 8)
            selected_message = y0[j] if self.R_inputs[j] == 0 else y1[j]

            results.append(bytes([(selected_message[k] ^ h_tj[k]) for k in range(self.n // 8)]))

        self.last_results = results

    def send_last_results(self):
        return self.last_results