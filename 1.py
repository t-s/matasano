import base64 as b64
import binascii

def strxor(s0, s1):
  l = [chr(ord(a) ^ ord(b)) for a,b in zip(s0, s1)]
  return ''.join(l)

# take in raw string, no hexadecimilization
def score(string_to_be_scored):
  max_score = -100
  best_so_far = ''
  for letter in map(chr, range(0, 255)):
    letter_list = letter*len(string_to_be_scored)
    plaintext_string = strxor(string_to_be_scored,letter_list)
    space_count = 0
    punctuation_count = 0
    for letter in plaintext_string:
      # as a first stab at how to score, just count spaces
      if letter == ' ':
        space_count = space_count + 1
      if (not letter.isalpha()):
        punctuation_count = punctuation_count - 1
    score = space_count + punctuation_count
    if score > max_score:
      max_score = score
      best_so_far = plaintext_string
  print best_so_far

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
encoded_string = binascii.a2b_hex(hex_string)
print encoded_string

s1 = "1c0111001f010100061a024b53535009181c"
s1 = binascii.unhexlify(s1)
s2 = "686974207468652062756c6c277320657965"
s2 = binascii.unhexlify(s2)
print strxor(s1,s2)

s3 = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
s3 = binascii.unhexlify(s3)
score(s3)

fopen = open('./1.dat','r')
for line in fopen:
  score(line.strip('\n'))

