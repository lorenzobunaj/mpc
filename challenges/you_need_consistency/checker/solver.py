from Crypto.Cipher import AES

def xor(a, b, l):
    return bytes([a[k] ^ b[k] for k in range(l)])

def decrypt_flag(enc_flag, seed):
    key = (seed * 2).encode()
    
    cipher = AES.new(key, AES.MODE_ECB)
    
    flag = cipher.decrypt(enc_flag)
    
    return flag

encrypted_flag = b'\x0e\xfeS,a\x14\x83\x16\xfd\xd6\xb6\x93\x16\xa9\x15\x00\x85\xba\xec8\xef<\xab\x85O\xc4\x14#\xd97\x98\x18'

# by sending r = '00000'
q1 = b"<\x81\r\xf9\xc0k\xf9\x1a6:m\xa2\xa3'\xcc\x00\xdaE\x9c&J\x8d\x12X\xc8\xed\xf2\xe5C\xfb^\xb2\xd5t\x05|\xd8\xa4\\7\xe2^\x83\xf3~\x12#2\x86v\xf5.$\xfbN\x9a\xee\xbe([4\x87\x18\xe1" + b'p\xec2\xeaZ!D\xd2C\xc0\xf1\x1e0\xc7\t\xc3\xd6\xfb3h\xff\xf6\xbb\xd6\xacH\x9f\xa5\xd8K\xdd\x94R\x1e\x9d\x1b\xa0Y\xfa\xfatd\xd6\x99\xb3\xbf\xad\xf8\x86[\xdd1w\xdd\xefEO\x98\xef3/\xb5\xe8n' + b"V\xc2\xd8\x97g\xfe\x1bq\xa39V\x8c3c\xb2a\xe8\xf4'\xb2\x11\x162\x864\xfc\x16_1\xa5\x7fIm\xd1\xc0w\xf6#\x8e\xdd\xbc\xbc\xdf\xda\x81\x1a\x98\x1f\xbf\xd4\x95Q\x94\x87\xbaN\x963a\xc1\xa2\xc9\x13O" + b'\xcd\x1d%\xad_\x91P\xffvW,\xa8\x8ba\x10\x90\x1d\xd5\x01\xd6\xb8\xa4\xad\xb0\xb1V_Q\xbas\xe6Zm+;+e\xb0D\xc9e\x10\xaex\xd3\x11L\x1d\xf21\xd1"\xcf\x9c7\xe23\xf0\xe4\t>\x8e\xd1\x9e' + b'\x0e5\x93\xf1\x86\xf7\xf9\x9aP9l>\xd8G\x053\x06\x08Z\x1dN\xb0\x18\x17\xf4\xbck>H\xb3\xcd\x96\xfc\xda9\x1c\xe0\x8e\x95o\xbc\xf6\xdeP\xa3\xf0\x1cZ\xf1\xa9\xc1\xb4e\x01H\x0fXk/\xa4\x0co\xcb\x9d'

# by sending r = '11111'
q2 = b'=\x81\x0c\xf9\xc0j\xf9\x1a6:m\xa3\xa3&\xcd\x00\xdaE\x9c&J\x8d\x12Y\xc9\xed\xf3\xe4C\xfb^\xb2\xd4t\x04|\xd8\xa5\\7\xe2_\x82\xf2~\x13#3\x86w\xf4.%\xfaN\x9b\xef\xbf(Z4\x86\x19\xe0' + b'q\xec3\xeaZ D\xd2C\xc0\xf1\x1f0\xc6\x08\xc3\xd6\xfb3h\xff\xf6\xbb\xd7\xadH\x9e\xa4\xd8K\xdd\x94S\x1e\x9c\x1b\xa0X\xfa\xfate\xd7\x98\xb3\xbe\xad\xf9\x86Z\xdc1v\xdc\xefDN\x99\xef2/\xb4\xe9o' + b'W\xc2\xd9\x97g\xff\x1bq\xa39V\x8d3b\xb3a\xe8\xf4\'\xb2\x11\x162\x875\xfc\x17^1\xa5\x7fIl\xd1\xc1w\xf6"\x8e\xdd\xbc\xbd\xde\xdb\x81\x1b\x98\x1e\xbf\xd5\x94Q\x95\x86\xbaO\x972a\xc0\xa2\xc8\x12N' + b'\xcc\x1d$\xad_\x90P\xffvW,\xa9\x8b`\x11\x90\x1d\xd5\x01\xd6\xb8\xa4\xad\xb1\xb0V^P\xbas\xe6Zl+:+e\xb1D\xc9e\x11\xafy\xd3\x10L\x1c\xf20\xd0"\xce\x9d7\xe32\xf1\xe4\x08>\x8f\xd0\x9f' + b'\x0f5\x92\xf1\x86\xf6\xf9\x9aP9l?\xd8F\x043\x06\x08Z\x1dN\xb0\x18\x16\xf5\xbcj?H\xb3\xcd\x96\xfd\xda8\x1c\xe0\x8f\x95o\xbc\xf7\xdfQ\xa3\xf1\x1c[\xf1\xa8\xc0\xb4d\x00H\x0eYj/\xa5\x0cn\xca\x9c'

seed_bits = xor(q1, q2, 8 * 8)

seed = ''
for i in range(0, len(seed_bits), 8):
    byte_bits = seed_bits[i:i + 8]
    byte = 0
    for bit in byte_bits:    
        byte = (byte << 1) | (1 if bit == 1 else 0)
    seed += chr(byte)

flag = decrypt_flag(encrypted_flag, seed).decode()

print("flag: " + flag)
