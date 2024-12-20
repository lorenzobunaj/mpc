LEN_FLAG = 28

def xor(a, b, l):
    return bytes([a[k] ^ b[k] for k in range(l)])

def solve():
    m = 8 * LEN_FLAG

    s = [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1]

    # first 2 seeds
    seeds = [b'9\x10\xf3y\xa9C{\x80', b'MO\x0e\xf2"AK\x81']

    # first 2 PRG(T[i])
    RTts = [[122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53, 122, 114, 5, 138, 228, 47, 83, 53], [56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67, 56, 254, 11, 229, 177, 105, 88, 67]]

    # first 2 u[i]
    us = [b'\x1f1G\x96\x05\xef\x80\xd4\x1f1G\x96\x04\xef\x81\xd4\x1f1G\x96\x05\xee\x81\xd5\x1f1G\x96\x05\xef\x80\xd5\x1f1G\x97\x04\xee\x80\xd5\x1f1F\x96\x04\xef\x80\xd4\x1f0G\x97\x05\xee\x80\xd5\x1f1G\x97\x05\xef\x80\xd4\x1f0G\x97\x05\xee\x80\xd5\x1f1G\x97\x05\xee\x80\xd4\x1f1F\x97\x04\xef\x80\xd5\x1f1F\x97\x05\xef\x81\xd4\x1f1G\x97\x05\xee\x80\xd4\x1f1G\x97\x05\xef\x81\xd5\x1f0G\x97\x05\xef\x81\xd5\x1f1G\x97\x05\xef\x81\xd4\x1f1F\x97\x04\xef\x80\xd5\x1f1F\x97\x05\xee\x80\xd4\x1f0G\x97\x05\xef\x81\xd4\x1f1G\x96\x04\xef\x80\xd4\x1f1G\x96\x05\xef\x81\xd4\x1f1G\x96\x04\xef\x80\xd5\x1f1G\x96\x04\xef\x81\xd5\x1f1G\x96\x04\xef\x80\xd4\x1f0G\x97\x05\xee\x80\xd5\x1f1G\x97\x05\xee\x80\xd5\x1f1G\x97\x05\xee\x80\xd5\x1f1G\x97\x04\xef\x81\xd5', b'6\xd2\xf2\xe4\xdeE:w6\xd2\xf2\xe4\xdfE;w6\xd2\xf2\xe4\xdeD;v6\xd2\xf2\xe4\xdeE:v6\xd2\xf2\xe5\xdfD:v6\xd2\xf3\xe4\xdfE:w6\xd3\xf2\xe5\xdeD:v6\xd2\xf2\xe5\xdeE:w6\xd3\xf2\xe5\xdeD:v6\xd2\xf2\xe5\xdeD:w6\xd2\xf3\xe5\xdfE:v6\xd2\xf3\xe5\xdeE;w6\xd2\xf2\xe5\xdeD:w6\xd2\xf2\xe5\xdeE;v6\xd3\xf2\xe5\xdeE;v6\xd2\xf2\xe5\xdeE;w6\xd2\xf3\xe5\xdfE:v6\xd2\xf3\xe5\xdeD:w6\xd3\xf2\xe5\xdeE;w6\xd2\xf2\xe4\xdfE:w6\xd2\xf2\xe4\xdeE;w6\xd2\xf2\xe4\xdfE:v6\xd2\xf2\xe4\xdfE;v6\xd2\xf2\xe4\xdfE:w6\xd3\xf2\xe5\xdeD:v6\xd2\xf2\xe5\xdeD:v6\xd2\xf2\xe5\xdeD:v6\xd2\xf2\xe5\xdfE;v', b'h\x8a\xd49\x873\x06fh\x8a\xd49\x863\x07fh\x8a\xd49\x872\x07gh\x8a\xd49\x873\x06gh\x8a\xd48\x862\x06gh\x8a\xd59\x863\x06fh\x8b\xd48\x872\x06gh\x8a\xd48\x873\x06fh\x8b\xd48\x872\x06gh\x8a\xd48\x872\x06fh\x8a\xd58\x863\x06gh\x8a\xd58\x873\x07fh\x8a\xd48\x872\x06fh\x8a\xd48\x873\x07gh\x8b\xd48\x873\x07gh\x8a\xd48\x873\x07fh\x8a\xd58\x863\x06gh\x8a\xd58\x872\x06fh\x8b\xd48\x873\x07fh\x8a\xd49\x863\x06fh\x8a\xd49\x873\x07fh\x8a\xd49\x863\x06gh\x8a\xd49\x863\x07gh\x8a\xd49\x863\x06fh\x8b\xd48\x872\x06gh\x8a\xd48\x872\x06gh\x8a\xd48\x872\x06gh\x8a\xd48\x863\x07g']

    PRG_KEY = b'\xe2\xde\x89 _\xe2\xb4A'

    PRG_KEY2 = b'\xa1\xbc\x7f\xd3\x12\x8e\x9c\xf4'

    '''
    since s[1] = 1, seeds[1] = KOT_seeds[1][1] * m // 8]

    by reversing the PRG, we can retrieve KOT_seeds[1][0] as
    
    KOT_seeds[1][0] = RTts[1] ^ [PRG_KEY * m // 8] ^ [PRG_KEY2 * m // 8]

    also, the PRG_KEY in u cancel each other leaving

    u = KOT_seeds[1][0] ^ KOT_seeds[1][1] ^ r

    so, we can discover r, which hides the FLAG, as 

    r = us[1] ^ KOT_seeds[1][0] ^ KOT_seeds[1][1]

    for s[0] = 0, that wouldn't work, since seeds[0] = KOT_seeds[0][0], so we can't get any additional information from RTts[0]

    '''

    seed = seeds[1]
    RTt = RTts[1]
    u = us[1]

    k1 = seed * (m // 8)

    k0 = xor(xor(RTt, PRG_KEY * (m // 8), m), PRG_KEY2 * (m // 8), m)

    r = xor(xor(u, k0, m), k1, m)
    
    flag = ""
    for i in range(0, len(r), 8):
        char_bits = r[i:i+8]
        char_value = sum(b << (7 - idx) for idx, b in enumerate(char_bits))
        flag += chr(char_value)

    print(f'flag: {flag}')

if __name__ == "__main__":
    solve()
