from utils import xor
import os

class Receiver:
    def __init__(self, K, r, l, m, n):
        '''
        - setup phase -
        assign the procotol parameters and initialize the instance variables
        '''

        self.K = K  # security parameter
        self.r = r # statistical security parameter
        self.l = l # number of base OT in the initial OT phase
        self.m = m  # number of base OT in the extension phase
        self.n = n  # lenght of each message

        self.R_inputs = []

        self.KOT_seeds = [(os.urandom(K // 8), os.urandom(K // 8)) for _ in range(l)]  # seeds in the initial OT phase
        self.T = None # matrix (m + r) x l in the extension phase

        self.strings = None # strings in the output phase

    def new_inputs(self, R_inputs):
        '''
        - setup phase -
        assign the new receiver inputs
        '''

        for i in range(self.m):
            self.R_inputs.append(R_inputs[i])

    def KOT_send(self):
        '''
        - initial OT phase -
        send the seeds to the KOT oracle
        '''

        return self.KOT_seeds

    def send_U(self, PRG):
        '''
        - extension phase 1 -
        compute U and send it
        '''

        tau = [0 for _ in range(self.r)]
        self.R_inputs = self.R_inputs + tau

        Tt = [PRG(self.KOT_seeds[i][0], self.m + self.r) for i in range(self.l)]
        U = [xor(self.m + self.r, Tt[i], PRG(self.KOT_seeds[i][1], self.m + self.r), self.R_inputs) for i in range(self.l)]

        self.T = list(zip(*Tt))

        return U
    
    def consistency_check(self, PRG, CR_HASH):
        '''
        - consistency check -
        compute the hashes and send them
        '''

        H = []
        for a in range(self.l):
            H.append([])
            for b in range(self.l):
                H[a].append([])
                H[a][b].append(CR_HASH(a, xor(self.m + self.r, PRG(self.KOT_seeds[a][0], self.m + self.r), PRG(self.KOT_seeds[b][0], self.m + self.r)), self.m + self.r))
                H[a][b].append(CR_HASH(a, xor(self.m + self.r, PRG(self.KOT_seeds[a][0], self.m + self.r), PRG(self.KOT_seeds[b][1], self.m + self.r)), self.m + self.r))
                H[a][b].append(CR_HASH(a, xor(self.m + self.r, PRG(self.KOT_seeds[a][1], self.m + self.r), PRG(self.KOT_seeds[b][0], self.m + self.r)), self.m + self.r))
                H[a][b].append(CR_HASH(a, xor(self.m + self.r, PRG(self.KOT_seeds[a][1], self.m + self.r), PRG(self.KOT_seeds[b][1], self.m + self.r)), self.m + self.r))

        return H

    def receive_masked_strings(self, y0, y1, CR_HASH):
        '''
        - extension phase 2 -
        receive masked strings and reconstruct the selected strings.
        '''

        strings = []
        for j in range(self.m):
            tj = self.T[j]
            h_tj = CR_HASH(j, tj, self.n // 8)
            selected_message = y0[j] if self.R_inputs[j] == 0 else y1[j]

            strings.append(bytes([(selected_message[k] ^ h_tj[k]) for k in range(self.n // 8)]))

        self.strings = strings

    def send_strings(self):
        '''
        - output phase -
        send the selected strings
        '''

        return self.strings