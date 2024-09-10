# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, codebet):
    new_str = ""
    for let in text:
        index = alpha.index(let)
        new_str += cipher_alphabet[(index) % 26]
    return new_str


def sub_decode(text, codebet):
    new_str = ""
    for let in text:
        index = cipher_alphabet.index(let)
        new_str += alpha[(index) % 26]
    return new_str



test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
