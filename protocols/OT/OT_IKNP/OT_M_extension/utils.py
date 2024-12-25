def xor(l, *args):
    xored_args = []

    for _ in range(l):
        res = 0
        for arg in args:
            res ^= arg

        xored_args.append(res)

    return bytes(xored_args)