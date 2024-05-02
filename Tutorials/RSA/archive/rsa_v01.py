#
# RSA encryption
#

import math
import random as rng

# Primes
P = 11
Q = 7
n = P * Q


# Eulers Phi Function
phi = (P - 1) * (Q - 1)


# Choose e greater than 1 and
# that the gcd of e and phi equals 1
e = 2
while(e < phi):
  if(math.gcd(e, phi) == 1):
    break

  else:
    e += 1




# Prime Functions
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


      




# Message Converting and encryption functions
msg_input = str(input('Enter Message: '))

def str_to_dec(msg: str):
  list_msg_dec = []
  for i in msg:
    list_msg_dec.append(ord(i))

  return list_msg_dec

def dec_to_str(bytelist: str):
  msg_str = ''
  for i in bytelist:
    msg_str += chr(i)

  return msg_str


str_bytelist = str_to_dec(msg_input)
print(str_bytelist)
print(dec_to_str(str_bytelist))
