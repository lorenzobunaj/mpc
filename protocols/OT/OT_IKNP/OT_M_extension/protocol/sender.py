from utils import xor
import os

class Sender:
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

        self.S_inputs = [] # sender inputs

        self.KOT_choice_bits = [int.from_bytes(os.urandom(1), byteorder="big") % 2 for _ in range(l)]  # choice bits in the initial OT phase
        self.KOT_choosen_seeds = None # choosen seeds in the initial OT phase
        
        self.U = None # (m + r) x l matrix U in the extension phase

    def new_inputs(self, S_inputs):
        '''
        - setup phase -
        assign the new sender inputs
        '''

        for i in range(self.m):
            self.S_inputs.append(S_inputs[i])

    def KOT_send(self):
        '''
        - initial OT phase -
        send the choice bits to the KOT oracle
        '''

        return self.KOT_choice_bits
    
    def KOT_receive(self, KOT_choosen_seeds):
        '''
        - initial OT phase -
        receive the chosen seeds from the KOT oracle
        '''

        self.KOT_choosen_seeds = KOT_choosen_seeds

    def receive_U(self, U):
        '''
        - extension phase 1 -
        receive U and use it to compute Q
        '''

        self.U = U

    def consistency_check(self, H, PRG, CR_HASH):
        '''
        - consistency check of R_inputs -
        receive the hashes and check their consistency
        '''

        hashes = []
        hashes_hat = []
        
        for a in range(self.l):
            hashes.append([])
            hashes_hat.append([])

            for b in range(a, self.l):
                hashes[a].append(CR_HASH(a, xor(self.m + self.r, PRG(self.KOT_choosen_seeds[a], self.m + self.r), PRG(self.KOT_choosen_seeds[b], self.m + self.r))))
                hashes_hat[a].append(CR_HASH(a, xor(self.m + self.r, PRG(self.KOT_choosen_seeds[a], self.m + self.r), PRG(self.KOT_choosen_seeds[b], self.m + self.r), self.U[a], self.U[b])))

        for a in range(self.l):
            for b in range(a, self.l):
                check1 = H[a][b][2*self.KOT_choice_bits[a] + self.KOT_choice_bits[b]] == hashes[a][b]
                check2 = H[a][b][2*(1-self.KOT_choice_bits[a]) + 1 - self.KOT_choice_bits[b]] == hashes_hat[a][b]
                check3 = self.U[a] != self.U[b]

                if not (check1 and check2 and check3):
                    return 0
        
        return 1


    def _compute_Q(self, PRG):
        '''
        - extension phase 2 -
        compute Q
        '''

        Qt = [
            bytes(
                [((self.KOT_choice_bits[i] * self.U[i][j]) ^ PRG(self.KOT_choosen_seeds[i], self.m + self.r)[j])
                for j in range(self.m + self.r)]
            )
            for i in range(self.l)
        ]

        return [bytes(row) for row in list(zip(*Qt))]

    def send_masked_strings(self, PRG, CR_HASH):
        '''
        - extension phase 2 -
        compute the masked strings and send it
        '''

        Q = self._compute_Q(PRG)

        y0 = []
        y1 = []

        for j in range(self.m):
            qj = Q[j]
            x0_j, x1_j = self.S_inputs[j]

            h0 = CR_HASH(j, qj, self.n // 8)
            h1 = CR_HASH(j, xor(qj, self.KOT_s, self.l), self.n // 8)

            y0.append(xor(x0_j, h0, self.n // 8))
            y1.append(xor(x1_j, h1, self.n // 8))
        
        return [y0, y1]
