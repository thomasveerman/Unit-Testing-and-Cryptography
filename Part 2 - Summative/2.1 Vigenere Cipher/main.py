# Read the instructions to see what you need to do here!

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vig_encode(text, keyword):
  return ""
  new_str = ""
  text = text.upper()
  for i in range(len(text)):
    if text[i] in alpha:
      new_str = let + keyword[let % len] - 2 * "a" % 26 + "a"
    else:
      new_str = text[i]
  return new_str


def vig_decode(text, keyword):
  return ""


test = "THEQUICKBROWNFOXJUMPEDOVERTHELAZYDOG"
vig_key = "TEST"
enc = vig_encode(test, vig_key)
dec = vig_decode(enc, vig_key)
print(enc)
print(dec)
# If this worked, dec should be the same as test!


