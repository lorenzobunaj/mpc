import os
from protocol.wrapper import start_protocol, protocol
from oracles import KOT
from primitives import PRG, CR_HASH
from secrets import FLAG

def main():
    K = 64
    l = K
    n = 16
    m = 5

    times = 0
    while True:
        S_inputs = [(os.urandom(n // 8), os.urandom(n // 8)) for _ in range(m)]
        R_inputs = [int.from_bytes(os.urandom(1), byteorder="big") % 2 for _ in range(m)]

        [S, R] = start_protocol(K, K, l, n, m)
        protocol(S, R, S_inputs, R_inputs, KOT, PRG, CR_HASH)

        R_inputs_guess = input("Enter the Receiver choice bits: ")
        R_inputs_guess = [int(b) for b in list(R_inputs_guess)]
        
        if (R_inputs_guess == R_inputs):
            times += 1

            if (times > 10):
                print("flag:")
                print(FLAG)
            else:
                print("good job")
                print(FLAG)
        else:
            print("Sorry, try again\n\n")

if __name__ == "__main__":
    main()
