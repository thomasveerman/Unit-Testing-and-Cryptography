import math

# Read the instructions to see what to do!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# PART 1
# These functions are provided for you!
def mod_inverse_helper(a, b):
    q, r = a//b, a % b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m


# These are the functions you'll need to write:
def affine_encode(text, a, b):
    result = ''
    for letter in text:
        x = alpha.index(letter)
        endcoded_letter = (a * x + b) % 26
        result += alpha[endcoded_letter]
    return result

def affine_decode(text, a, b):
    result = ''
    inverse_a = mod_inverse(a,26)
    for letter in text:
        y = alpha.index(letter)
        decoded_letter = (inverse_a * (y - b)) % 26
        result += alpha[decoded_letter]
    return result

test = "HELLOWORLD"
a = 3
b = 9
enc = affine_encode(test, a, b)
dec = affine_decode(enc, a, b)
print(enc)
print(dec)
# If this worked, dec should be the same as test!



# PART 2
# These  are the functions you'll need to write:
def convert_to_num(ngram):
    num = 0
    length = len(ngram)
    for i in range(length):
        num += alpha.index(ngram[i]) * (26 ** (length - i - 1))
    return num

def convert_to_text(num, n):
    result = ''
    for i in range(n):
        remainder = num % 26
        result = alpha[remainder] + result
        num //= 26
    return result

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
num = convert_to_num(test)
answer = convert_to_text(num, len(test))
print(num)
print(answer)
# If this worked, answer should be the same as test!



# PART 3

# These are the functions you'll need to write:
def affine_n_encode(text, n, a, b):
    while len(text) % n != 0:
        
        text += 'X'

    result = ''
    for i in range(0, len(text), n):
        ngram = text[i:i+n]
        x = convert_to_num(ngram)
        encoded_num = (a * x + b) % (26 ** n)
        result += convert_to_text(encoded_num, n)
    return result

def affine_n_decode(text, n, a, b):
    result = ''
    inverse_a = mod_inverse(a, 26 ** n)
    for i in range(0, len(text), n):
        ngram = text[i:i+n]
        y = convert_to_num(ngram)
        decoded_num = (inverse_a * (y - b)) % (26 ** n)
    return result

test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
n = 5
a = 347
b = 1721
enc = affine_n_encode(test, n, a, b)
dec = affine_n_decode(enc, n, a, b)
print(enc, dec)
# If this worked, dec should be the same as test!