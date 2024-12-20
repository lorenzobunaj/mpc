from Crypto.Hash import SHA256

def PRG(seed, m):
    """
    Pseudorandom generator

    PRG : {0, 1}^K -> {0, 1}^m
    """

    PRG_KEY = b'\xe2\xde\x89 _\xe2\xb4A'

    seed = seed * (m // len(seed))
    PRG_KEY = PRG_KEY * (m // len(PRG_KEY))
    
    state = []
    for (s, k) in zip(seed, PRG_KEY):
        x1 = s & k
        x2 = s | k
        x3 = s ^ k
        x4 = x2 & ~x1
        x5 = (x3 | x4) ^ (x1 & x2)
        x6 = ((x5 & x2) ^ x3) | (x4 & ~x5)
        x7 = (x6 ^ x2) & (~x4 | x1)
        final = x7 ^ x3

        state.append(final)

    output = state[:m]

    return output

def PRG_more_random(seed, m):
    """
    Pseudorandom generator

    PRG : {0, 1}^K -> {0, 1}^m
    """

    PRG_KEY = b'\xa1\xbc\x7f\xd3\x12\x8e\x9c\xf4'

    seed = seed * (m // len(seed))
    PRG_KEY = PRG_KEY * (m // len(PRG_KEY))

    state = []
    for (s, k) in zip(seed, PRG_KEY):
        x1 = s & k
        x2 = s | k
        x3 = s ^ k
        x4 = x2 & ~x1
        x5 = (x3 | x4) ^ (x1 & x2)
        x6 = ((x5 & x2) ^ x3) | (x4 & ~x5)
        x7 = (x6 ^ x2) & (~x4 | x1)
        final = x7 ^ x3

        state.append(final)

    output = state[:m]

    return output

def CR_HASH(index, input_data, n):
    """
    Correlation robust hash function

    CR_HASH: [m] x {0,1}^l -> {0,1}^n
    """
    
    if isinstance(input_data, tuple):
        input_data = b''.join(int.to_bytes(x, 1, byteorder='big') for x in input_data)  # Convert integers to bytes
    elif not isinstance(input_data, bytes):
        raise TypeError(f"Expected input_data to be bytes or tuple, got {type(input_data)}")
    
    hasher = SHA256.new()
    hasher.update(index.to_bytes(4, byteorder="big"))  # Represent index as 4 bytes
    hasher.update(input_data)
    return hasher.digest()[:n]