import base64
import binascii
import string

# -------------------------------
# Custom Base62 decoder with custom alphabet (bash62 support)
def decode_base62_custom(s, alphabet):
    base = len(alphabet)
    num = 0
    for char in s:
        num *= base
        if char not in alphabet:
            raise ValueError(f"Invalid character '{char}' for Base62.")
        num += alphabet.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, 'big')

# -------------------------------
# Decoders
def decode_base64(s):
    s += '=' * ((4 - len(s) % 4) % 4)
    return base64.b64decode(s)

def decode_base32(s):
    s += '=' * ((8 - len(s) % 8) % 8)
    return base64.b32decode(s)

def decode_ascii85(s):
    # If input has <~ ~> markers, treat as Adobe Ascii85
    if s.startswith('<~') and s.endswith('~>'):
        return base64.a85decode(s, adobe=True)
    else:
        return base64.a85decode(s, adobe=False)

def decode_hex(s):
    return bytes.fromhex(s)

def decode_binary(s):
    return int(s, 2).to_bytes((len(s) + 7) // 8, 'big')

# -------------------------------
# Manual Base58 decoder
BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

def decode_base58(s):
    num = 0
    for char in s:
        num *= 58
        if char not in BASE58_ALPHABET:
            raise ValueError("Invalid Base58 character")
        num += BASE58_ALPHABET.index(char)
    return num.to_bytes((num.bit_length() + 7) // 8, 'big')

# -------------------------------
# Manual Base62 decoder (bash62)
def decode_base62(s):
    bash62_alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return decode_base62_custom(s, alphabet=bash62_alphabet)

# -------------------------------
# Manual Base91 decoder
BASE91_ALPHABET = (
    "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    "0123456789!#$%&()*+,./:;<=>?@[]^_`{|}~\""
)

def decode_base91(data):
    v = -1
    b = 0
    n = 0
    out = bytearray()

    for char in data:
        if char not in BASE91_ALPHABET:
            raise ValueError("Invalid Base91 character")
        c = BASE91_ALPHABET.index(char)
        if v < 0:
            v = c
        else:
            v += c * 91
            b |= v << n
            n += 13 if (v & 8191) > 88 else 14
            while n > 7:
                out.append(b & 255)
                b >>= 8
                n -= 8
            v = -1
    if v != -1:
        out.append((b | v << n) & 255)
    return bytes(out)

# -------------------------------
# Generic decode wrapper
def try_decode(name, func, s):
    try:
        result = func(s)
        print(f"[✓] {name}:\n{result.decode('utf-8', errors='replace')}\n")
    except Exception as e:
        print(f"[x] {name} failed.")

# -------------------------------
# Main
if __name__ == "__main__":
    input_str = input("Enter encoded string: ").strip()
    print()

    try_decode("Base64", decode_base64, input_str)
    try_decode("Base32", decode_base32, input_str)
    try_decode("Base58", decode_base58, input_str)
    try_decode("Base62 (bash62)", decode_base62, input_str)
    try_decode("Base91", decode_base91, input_str)
    try_decode("Hexadecimal", decode_hex, input_str)
    try_decode("Binary", decode_binary, input_str)
    try_decode("Ascii85", decode_ascii85, input_str)

