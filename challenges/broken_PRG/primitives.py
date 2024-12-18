from Crypto.Hash import SHA256

def PRG(seed, m):
    """
    Pseudorandom generator using SHA256.

    PRG : {0, 1}^K -> {0, 1}^m
    """
    constants = [12, ]

    output = b""
    while len(output) < m:
        seed = SHA256.new(seed).digest()
        output += seed
    return output[:m]

def CR_HASH(index, input_data, n):
    """
    Correlation robust hash function.

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