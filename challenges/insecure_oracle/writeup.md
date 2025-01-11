# Insecure Oracle

### 1. Key Functions in the Code

#### **PRG (Pseudorandom Generator)**
The `PRG` function generates a pseudorandom string of length `m` given a seed using the SHA256 hash function. It expands the seed into a longer pseudorandom bit sequence:

```python
def PRG(seed, m):
    output = b""
    while len(output) < m:
        seed = SHA256.new(seed).digest()
        output += seed
    return output[:m]
```
- **Input:** A seed and the desired output length `m`.
- **Output:** A pseudorandom bitstring of length `m`.

#### **CR_HASH (Correlation Robust Hash)**
This function implements a correlation-robust hash function:

```python
def CR_HASH(index, input_data, n):
    if isinstance(input_data, tuple):
        input_data = b''.join(int.to_bytes(x, 1, byteorder='big') for x in input_data)
    elif not isinstance(input_data, bytes):
        raise TypeError(f"Expected input_data to be bytes or tuple, got {type(input_data)}")

    hasher = SHA256.new()
    hasher.update(index.to_bytes(4, byteorder="big"))
    hasher.update(input_data)
    return hasher.digest()[:n]
```
- **Input:** An `index`, some `input_data`, and the desired output length `n`.
- **Output:** A hash value truncated to length `n`.
- The function combines the `index` (converted to bytes) and the input data into a single hash computation.

#### **xor Function**
This function computes the XOR of multiple byte arrays efficiently:

```python
def xor(l, *args):
    if len(args) == 2:
        return xor2(args[0], args[1], l)
    else:
        return xor(l, xor2(args[0], args[1], l), *args[2:])
```
- **Input:** A length `l` and multiple byte arrays.
- **Output:** The XOR of all input byte arrays.

### 2. Solution Logic

#### **Problem Description**
The goal is to recover the receiver's input `r` from the protocol. The receiver's input `r` is extended by appending a sequence `tau` of zeros to produce `r'`. The recovery process relies on the Consistency Check, which acts as an oracle that verifies if a given candidate `r'` matches the receiver's extended input.

#### **Key Observations in the Solution**
- The variable `tau` is pre-determined as a sequence of zeros of length 64.
- The candidate `r` is guessed recursively using a binary tree approach.
- For each candidate `r`:
  - `r'` is formed by appending tau.
  - The pseudorandom values `G[0]` and `G[1]` are generated from the receiver's seeds.
  - The XOR operations and hash verification are performed to check if the candidate matches.

#### **Recursive Guessing**
The `guess_r` function performs a depth-first search to guess all possible combinations of the bits of `r`:

```python
def guess_r(rt):
    if len(rt) == 5:
        check_r(rt)
    else:
        guess_r(rt + [0])
        guess_r(rt + [1])
```
- **Base Case:** When the candidate `r` has 5 bits, it is passed to the `check_r` function.
- **Recursive Step:** For each bit position, the function tries both 0 and 1, exploring all possible candidates.

#### **Consistency Check**
The `check_r` function verifies if the guessed `r` is correct:

```python
def check_r(rt):
    rt = rt + tau

    G = [PRG(KOT_seeds[0], m + len_r), PRG(KOT_seeds[1], m + len_r)]

    if Hab[2 * (1 - KOT_choice_bits[0]) + KOT_choice_bits[1]] == CR_HASH(0, xor(m + len_r, Ua, rt, G[0], G[1]), m + len_r):
        print(rt)
```
- **Steps:**
  1. Extend `r` by appending `tau`.
  2. Compute pseudorandom values `G[0]` and `G[1]`.
  3. Compute the XOR of all relevant values.
  4. Check if the hash matches the expected value in `Hab`.


### Summary
The code systematically guesses the input `r` using the protocol's structure and consistency check to verify correctness. The cryptographic components (PRG, correlation-robust hash) ensure security under normal circumstances, but the oracle-based attack leverages the verification process to deduce `r`.
