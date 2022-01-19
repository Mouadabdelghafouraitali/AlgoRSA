# 1 - choose two primes randomly (e.g. 1 3 5 9 ...) number P,Q
# 2 - Compute N = P x Q
# 3 - Compute Phi(n) = (P - 1) x (Q - 1)
# 4 - Choose e, 1 > e > Phi  + GCD (Phi(n)) if result is 1 then e = the GCD of Phi(n)
# 5 - Public key = (e,n)
# 6 - Private key = (d,n) | d = e^-1 mod Phi(n)
# 7 - Encryption : C = m^e mod N
# 8 - Decryption : m = c^d mod n

import random
import sys

import rsa
from sympy import *


# Choose two primes randomly number P,Q

def get_random_prime():
    primes = [i for i in range(1, 20) if isprime(i)]
    return random.choice(primes)


p = get_random_prime()
q = get_random_prime()

# Compute N = P x Q
n = p * q

# Compute Phi(n) = (P - 1) x (Q - 1)
phi_n = (p - 1) * (q - 1)


# 4 - Choose e, 1 > e > Phi  + GCD (Phi(n)) if result is 1 then e = the GCD of Phi(n)

def get_e(phi_n):
    # e, 1 > e > Phi
    e = random.randrange(1, phi_n)
    g = gcd(e, phi_n)
    # keep looping till the e = 1
    while g != 1:
        e = random.randrange(1, phi_n)
        g = gcd(e, phi_n)
    return e


e = get_e(phi_n)

# Public key = (e,n)
print("Public key are [ e = {} and n = {} ]".format(e, n))


# Private key = (d,n)  | d = e^-1 mod Phi(n)
def get_d(e, phi_n):
    return mod_inverse(e, phi_n)


d = get_d(e, phi_n)
print("Private key are [ d = {} and n = {} ]".format(d, n))


# Encryption : c = m^e mod n

def encrypt(plaintext):
    # ord =  Return the Unicode code point for a one-character string
    cipher = []
    for m in plaintext:
        cipher.append(pow(ord(m), e) % n)
    return cipher


plaintext = input("Please enter text to encrypt : ")
ciphertext = encrypt(plaintext)
print("Encryption of {} is {}".format(plaintext, ciphertext))


# Decryption : m = c^d mod n

def decrypt(ciphertext):
    message = []
    # chr = Return a Unicode string of one character with ordinal i
    for c in ciphertext:
        message.append(chr((int(c) ** d) % n))
    return message


message = decrypt(ciphertext)
print("Decryption of {} is {}".format(ciphertext, message))
