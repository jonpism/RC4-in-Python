#  key scheduling
def ksa(seed):
  S = []
  j = 0
  for i in range(0, 32):
    S.append(i)
  for i in range(0, 32):
    j = (j + S[i] + seed[i % len(seed)]) % 32
    S[i], S[j] = S[j], S[i]
  return S

#  Pseudo-random generation algorithm
def prga(S, plen):
  i = 0
  j = 0
  K = 0
  key_stream = []
  while plen > 0:
    i = (i + 1) % 32
    j = (j + S[i]) % 32
    S[i], S[j] = S[j], S[i]
    K = S[(S[i] + S[j]) % 32]
    key_stream.append(K)
    plen -= 1
  return key_stream

# XOR operation/function for encryption and decryption
def XOR(text_stream, key_stream):
  txt_stream = []
  for i in range(len(key_stream)):
    txt_stream.append(key_stream[i] ^ text_stream[i])
  return txt_stream

# USER INPUTS:
key = input("Give key: ")
plaintext = input("Give plaintext: ")

# seed (key array):
TABLE = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 
         'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 
         'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 
         'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
         'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30, 
         'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 
         'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41, 'q': 42,
         'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48,
         'x': 49, 'y': 50, 'z': 51, '.': 52, '!': 53, '?': 54,
         '(': 55, ')': 56, '-': 57, ' ': 58}

seed = []
i = 0
while len(seed) <= len(TABLE):
  if key[i % len(key)] in TABLE:
    seed.append(TABLE[key[i % len(key)]])
    i += 1

# key stream using pseudo random number generator algorithm
# converting stream values to str values
key_stream = prga(ksa(seed), len(plaintext))

# plaintext (stream) array
plaintext_stream = []
i = 0
while len(plaintext_stream) < len(plaintext):
  if plaintext[i % len(plaintext)] in TABLE:
    plaintext_stream.append(TABLE[plaintext[i % len(plaintext)]])
    i += 1


print("========= |< ENCRYPTION >| =========")
# XOR operation with key_stream and plaintext_stream to encrypt the message
# and produce the ciphertext stream
ciphertext_stream = XOR(plaintext_stream, key_stream)

# converting ciphertext_stream values to str values
ciphertext = []
i = 0
while i < len(ciphertext_stream):
  for key, value in TABLE.items():
    if ciphertext_stream[i] == value:
      ciphertext.append(key)
  i += 1

# printing the ciphertext
print("Ciphertext: ", end='')
for i in range(len(ciphertext)):
  print(ciphertext[i], end='')
print(end='\n')


print("========= |< DECRYPTION >| =========")
# decryption: using the same XOR operation as the encryption
# and converting the stream values to str values
decryption_stream = XOR(ciphertext_stream, key_stream)
decryption_str = []
for i in range(len(decryption_stream)):
  for key, value in TABLE.items():
    if decryption_stream[i] == value:
      decryption_str.append(key)
  
# printing the decrypted message
print("Decrypted message: ", end='')
for i in range(len(decryption_str)):
  print(decryption_str[i], end='')

