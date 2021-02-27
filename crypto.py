IP = [2, 6, 3, 1, 4, 8, 5, 7]
EP = [4, 1, 2, 3, 2, 3, 4, 1]
P8 = [6, 3, 7, 4, 8, 5, 10, 9]
P4 = [2, 4, 3, 1]
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
IP_inverse = [4, 1, 3, 5, 7, 2, 8, 6]
S0 = [[1, 0, 3, 2],[3, 2, 1, 0],[0, 2, 1, 3],[3, 1, 3, 2]]
LS_1, LS_2 = 1, 2

plaintext=input("Enter the plaintext:")
key=input("Enter the key:")
print("What you want to use to encrypt the plaintext \n 1. Original S1 \n 2. Modiﬁed S1")
input_S1 = input("Select 1 or 2: ")

if input_S1 == "1":
  S1= [[0, 1, 2, 3],[2, 0, 1, 3],[3, 0, 1, 0],[2, 1, 0, 3]]
else:
  S1= [[2, 1, 0, 3],[2, 0, 1, 3],[0, 1, 2, 3],[2, 1, 0, 3]]

def swap(x,y):
    return y,x

def permutate(text, key):
    data=""
    for i in key:
        data+=text[i-1]
    return data

def xor(bits, key):
    data = ''
    for bit, key_bit in zip(bits, key):
        data += str(((int(bit) + int(key_bit)) % 2))
    return data

def looks_up_sbox(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return '{0:02b}'.format(sbox[row][col])

def key_generation(permute, t):
  left, right = permute[:5], permute[5:]
  left_shift = left[t:5] + left[:t]
  right_shift = right[t:5] + right[:t]
  key_shift = left_shift + right_shift
  key = permutate(key_shift, P8)
  return key, key_shift

def encryption(right,left,key):
  right = permutate(right, EP)
  x = xor(right, key)
  lefthalf = x[:4]
  right = x[4:]
  lefthalf = looks_up_sbox(lefthalf, S0)
  right = looks_up_sbox(right, S1)
  right = lefthalf + right
  new = permutate(right, P4)
  return xor(left, new)

def decryption(right,left,key):
  right = permutate(right, EP)
  x = xor(right, key)
  lefthalf = x[:4]
  righthalf = x[4:]
  lefthalf = looks_up_sbox(lefthalf, S0)
  righthalf = looks_up_sbox(righthalf, S1)
  right = lefthalf + righthalf
  new = permutate(right, P4)
  return xor(left, new)

permute = permutate(key,P10)                        #permutation
key1, key_shift = key_generation(permute, LS_1)     #generation of key k1
key, p = key_generation(key_shift, LS_2)            #generation of key k2
key2 = permutate(p, P8)

new = permutate(plaintext, IP)                      #permutation
right, left = new[4:], new[:4]
left = encryption(right,left,key1)                  #SDES encryption round 1
left, right = swap(left, right)
print("Intermediate result after SW:", left + right)
left = encryption(right,left,key2)                  #SDES encryption round 2
x = left + right
ciphertext = permutate(x, IP_inverse)
print("The cipher text is ", ciphertext)

new = permutate(ciphertext, IP)                     #permutation
right, left = new[4:], new[:4]

left = decryption(right,left,key2)                  #SDES decryption round 1
left, right = swap(left, right)
print("Intermediate result after SW:", left + right)

left = decryption(right,left,key1)                  #SDES decryption round 2
x = left + right
plaintext = permutate(x, IP_inverse)
print("The plain text is ", plaintext)

