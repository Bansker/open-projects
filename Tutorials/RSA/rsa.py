#
#
#
# RSA encryption
#
#
#

import math
import random as rng


class RSAEncryption:
  def init(self):
  






#
# Prime and keygen functions
#
def is_prime(n):
  if(n <= 1):
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return False

  return True
  

def generate_prime():
  while(True):
    rand_num = rng.randint(2 ** 8, 2 ** 16)
    if is_prime(rand_num):
      return rand_num


def generate_keypair():
  p = generate_prime()
  q = generate_prime()
  n = p * q
  phi = (p - 1) * (q - 1)

  while(True):
    e = rng.randint(2, phi)
    if math.gcd(e, phi) == 1:
      break

  d = pow(e, -1, phi)
  return((n, e), (n, d))



def encrypt(msg, pub_key):
  n, e = pub_key
  msg_encr = [pow(ord(char), e, n) for char in msg]
  return msg_encr

def decrypt(msg_encr, pvt_key):
  n, d = pvt_key
  msg_decr = ''.join([chr(pow(char, d, n)) for char in msg_encr])
  return msg_decr



# Message Converting and encryption functions
msg_input = str(input('\nEnter Message: '))

pub_key, pvt_key = generate_keypair()
print(f'pub: {pub_key}, pvt: {pvt_key}\n')

msg_encrypted = encrypt(msg_input, pub_key)
print(f'Encrypted message: \n{msg_encrypted}\n')

msg_decrypted = decrypt(msg_encrypted, pvt_key)
print(f'Decrypted message: \n{msg_decrypted}\n')

