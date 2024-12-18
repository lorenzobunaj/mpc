from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def KOT(S_input_func, R_input_func, R_output_func):
    """
    Simulates K-OT using RSA encryption for secure 1-out-of-2 OT.

    :param S_input_func: A function where the sender provides its inputs (seeds as pairs).
    :param R_input_func: A function where the receiver provides its input (selection bits).
    :param R_output_func: A function where the receiver receives its selected outputs.
    """
    
    rsa_keys = RSA.generate(1024)
    public_key = rsa_keys.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    decipher = PKCS1_OAEP.new(rsa_keys)

    seeds = S_input_func()

    choices = R_input_func()

    # Step 3: Sender encrypts seed pairs using RSA
    encrypted_seeds = []
    for k0, k1 in seeds:
        encrypted_k0 = cipher.encrypt(k0)
        encrypted_k1 = cipher.encrypt(k1)
        encrypted_seeds.append((encrypted_k0, encrypted_k1))

    # Step 4: Receiver decrypts the selected seed based on its choice
    output = []
    for i, choice in enumerate(choices):
        encrypted_k0, encrypted_k1 = encrypted_seeds[i]
        if choice == 0:
            selected_seed = decipher.decrypt(encrypted_k0)
        else:
            selected_seed = decipher.decrypt(encrypted_k1)
        output.append(selected_seed)

    # Step 5: Receiver receives the selected outputs
    R_output_func(output)
