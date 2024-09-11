# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sub_encode(text, cipher_alphabet):
    text = text.upper()
    new_str = ""
    for let in text:
        if let in alpha:
            index = alpha.index(let)
            new_str += cipher_alphabet[index]
        else:
            new_str += let
    return new_str


def sub_decode(text, cipher_alphabet):
    text = text.upper()
    new_str = ""
    for let in text:
        if let in cipher_alphabet:
            index = cipher_alphabet.index(let)
            new_str += alpha[index]
        else:
            new_str += let
    return new_str


test = "HELLOWORLD"
cipher_alphabet = "WJKUXVBMIYDTPLHZGONCRSAEFQ"
enc = sub_encode(test, cipher_alphabet)
dec = sub_decode(enc, cipher_alphabet)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
