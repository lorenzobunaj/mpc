from sender import Sender
from receiver import Receiver
from oracles import KOT
from primitives import PRG, CR_HASH
from test_cases.OT_sh_protocol_test import OT_sh_protocol_test
import os

def main():
    OT_sh_protocol_test()

if __name__ == "__main__":
    main()
