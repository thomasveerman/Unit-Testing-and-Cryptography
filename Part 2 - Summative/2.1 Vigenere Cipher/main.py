# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  text = text.upper()
  encoded_message = ""
  keyword_repeated = ""
  for i in range(len(text)):
    keyword_repeated += keyword[i % len(keyword)]
  for i in range(len(text)):
    message_index = alpha.index(text[i])
    keyword_index = alpha.index(keyword_repeated[i])
    encoded_index = (message_index + keyword_index) % 26
    encoded_message += alpha[encoded_index]
  return encoded_message


def vig_decode(text, keyword):
  text = text.upper()
  decoded_message = ""
  keyword_repeated = ""
  for i in range(len(text)):
    keyword_repeated += keyword[i % len(keyword)]
  for i in range(len(text)):
    encoded_index = alpha.index(text[i])
    keyword_index = alpha.index(keyword_repeated[i])
    decoded_index = (encoded_index - keyword_index) % 26
    decoded_message += alpha[decoded_index]
  return decoded_message


test = "thecatwaslazyandtired"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!


