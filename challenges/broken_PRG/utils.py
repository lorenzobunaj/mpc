def xor(a, b, l):
    return bytes([a[k] ^ b[k] for k in range(l)])