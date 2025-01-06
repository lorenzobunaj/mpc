def xor2(a, b, l):
    return bytes([a[k] ^ b[k] for k in range(l)])

def xor(l, *args):
    if len(args) == 2:
        return xor2(args[0], args[1], l)
    else:
        return xor(l, xor2(args[0], args[1], l), *args[2:])