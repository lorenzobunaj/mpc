LEN_FLAG = 28

def xor(a, b, l):
    return bytes([a[k] ^ b[k] for k in range(l)])

def solve():
    m = 8 * LEN_FLAG

    s = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1]

    seed = b'\xc4r\xf4\xe8\xe9\x94~\x8d'

    RTt = [78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105, 78, 161, 118, 196, 221, 128, 155, 105]

    u = b'\xc9\xb1t\xdfyx\xcdQ\xc9\xb1t\xdfyx\xcdQ\xc9\xb1t\xdfyx\xcdQ\xc9\xb1t\xdfxy\xccP\xc8\xb0t\xdeyy\xccP\xc8\xb0t\xdexy\xcdP\xc8\xb0u\xdeyy\xccP\xc8\xb0u\xdexx\xccP\xc8\xb0t\xdfxy\xccP\xc9\xb1u\xdexy\xccP\xc8\xb0u\xdeyx\xcdQ\xc8\xb1u\xdexy\xccP\xc8\xb0u\xdexy\xccQ\xc9\xb1t\xdfxy\xccP\xc9\xb0t\xdfxy\xcdQ\xc9\xb1u\xdfyx\xcdQ\xc8\xb1t\xdeyy\xccP\xc9\xb1t\xdexy\xcdP\xc9\xb0t\xdeyx\xccP\xc9\xb0u\xdexx\xccP\xc8\xb0u\xdeyx\xcdP\xc8\xb1t\xdexy\xccP\xc8\xb0u\xdfxx\xcdQ\xc8\xb0t\xdeyy\xcdP\xc8\xb0u\xdfyx\xccP\xc8\xb1u\xdfxx\xccQ\xc9\xb0u\xdfxx\xcdQ\xc9\xb0u\xdfxy\xccP'

    PRG_KEY = b'\xe2\xde\x89 _\xe2\xb4A'

    PRG_KEY2 = b'\xa1\xbc\x7f\xd3\x12\x8e\x9c\xf4'

    '''
    since s[0] = 1, seed = KOT_seeds[0][1] * m // 8]

    by reversing the PRG, we can retrieve KOT_seeds[0][0] as
    
    KOT_seeds[0][0] = RTt[0] ^ [PRG_KEY * m // 8] ^ [PRG_KEY2 * m // 8]

    also, the PRG_KEY in u cancel each other leaving

    u = KOT_seeds[0][0] ^ KOT_seeds[0][1] ^ r

    so, we can discover r, which hides the FLAG, as 

    r = u ^ KOT_seeds[0][0] ^ KOT_seeds[0][1]
    '''

    k1 = seed * (m // 8)

    k0 = xor(xor(RTt, PRG_KEY * (m // 8), m), PRG_KEY2 * (m // 8), m)

    r = xor(xor(u, k0, m), k1, m)

    print(bytes(r))

if __name__ == "__main__":
    solve()
