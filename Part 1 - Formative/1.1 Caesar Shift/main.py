# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def caesar_encode(text, n):
    # checks if text in text
    if not text:
        return ""
    # makes it uppercase
    text = text.upper()
    new_str = ""
    # finds letter in text
    for let in text:
        if let in alpha:
            # finds letter and adds it to new_str
            index = alpha.index(let)
            new_str += alpha[(index + n) % 26]
        else:
            # if letter not in alpha it just adds the letter as is
            new_str += let

    return new_str


def caesar_decode(text, n):
    # makes it uppercase

    text = text.upper()
    new_str = ""

    for let in text:
        if let in alpha:
            # finds letter and adds it to new_str
            index = alpha.index(let)
            new_str += alpha[(index - n) % 26]
        else:
            new_str += let

    return new_str


test = "thomas"
shift = 5
enc = caesar_encode(test, shift)
dec = caesar_decode(enc, shift)
print(enc)
print(dec)
# If this worked, dec should be the same as test!
