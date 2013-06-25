import base64 as b64
import string
import binascii

def hamming(left, right):
    left_string = ""
    right_string = ""
    diffs = 0

    for a in left: 
        bin_chars = bin(ord(a)).lstrip('0b')
        if len(bin_chars) < 7:
            bin_chars = "0" + bin_chars
        left_string += bin_chars
    for b in right: 
        bin_chars = bin(ord(b)).lstrip('0b')
        if len(bin_chars) < 7:
            bin_chars = "0" + bin_chars
        right_string += bin_chars

    for n in range(max(len(left_string),len(right_string))):
        if n >= len(left_string) or n >= len(right_string):
            diffs = diffs + 1
            break
        if(left_string[n] != right_string[n]):
            diffs = diffs + 1

def re_xor_encrypt(key, input_string):
    output_string = ""
    for n in range(len(input_string)):
        output_string += strxor(key[n%len(key)],input_string[n])
    print binascii.hexlify(output_string)

def re_xor_decrypt():
    pass

def strxor(left, right):
  letter = [chr(ord(a) ^ ord(b)) for a,b in zip(left, right)]
  return ''.join(letter)

# take in raw string, no hexadecimilization
def score(string_to_be_scored):
  for letter in map(chr, range(0, 255)):
    punctuation_count = 0
    letter_count = 0
    digit_count = 0
    space_count = 0
    bad = False
    
    letter_list = letter*len(string_to_be_scored)
    plaintext_string = strxor(string_to_be_scored,letter_list)
    
    for letter in plaintext_string:
      if ord(letter) < 32 and ord(letter) != 10:
        bad = True  
      elif ord(letter) > 126:
        bad = True
      if letter in string.punctuation:
        punctuation_count = punctuation_count + 1
      elif letter.isalpha():
        letter_count = letter_count + 1
      elif letter.isdigit():
        digit_count = digit_count + 1
      elif ord(letter) == 32:
        space_count = space_count + 1
    
    if(digit_count > letter_count):
       bad = True
    elif(punctuation_count > letter_count):
       bad = True
    elif(punctuation_count + digit_count > letter_count):
       bad = True
    elif(space_count == 0):
       bad = True
    elif punctuation_count > space_count:
       bad = True
    if bad == False:
       print plaintext_string.strip('\n')

def encode(key):
    for letter in key:
        pass

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


fopen = open('./first_round.dat','r')
i = 0
for line in fopen:
  score(binascii.unhexlify(line.strip('\n')))

input_string = "Burning 'em, if you ain't quick and nimble \
I go crazy when I hear a cymbal"
re_xor_encrypt("ICE",input_string)  

hamming("this is a test","wokka wokka!!!")
