#
# RSA encryption
#

import math


# Select 2 prime numbers, preferably large, p and q
p = 3
q = 7


# Calculate n = p*q
n = p * q
print("n = ", n)


# Calculate phi(n) = (p-1)*(q-1)
phi = (p - 1) * (q - 1)


# Choose a value of e such that
# 1<e<phi(n) and gcd(phi(n), e) = 1
e = 2
while(e < phi):
  if(math.gcd(e, phi) == 1):
    break

  else:
   e += 1

print("e =", e)


# Calculate d such that d = (e^-1) mod phi(n)
k = 2
d = ((k * phi) + 1) / e
print("d = ", d)
print(f'\nPublic key: {e, n}')
print(f'Private key: {d, n}')


# Plain Text
msg = int(input("Enter Message: "))
print("\nOriginal Message: ", msg)


# Encryption
c = pow(msg, e)
c = math.fmod(c, n)
print(f'Encrypted Message: {c}')


# Decryption
m = pow(c, d)
m = math.fmod(m, n)
print(f'Decrypted Message: {m}')
