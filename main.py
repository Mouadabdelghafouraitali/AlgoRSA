# 1 - choose two primes randomly (e.g. 1 3 5 9 ...) number P,Q
# 2 - Compute N = P x Q
# 3 - Compute Phi(n) = (P - 1) x (Q - 1)
# 4 - Choose e, 1 > e > Phi  + GCD (Phi(n)) if result is 1 then e = the GCD of Phi(n)
# 5 - Public key = (e,n)
# 6 - Private key = (d,n) | d = e^-1 mod Phi(n)
# 7 - Encryption : C = m^e mod N
# 8 - Decryption : m = c^d mod n


import random
from sympy import *


# Choose two primes randomly number P,Q

def get_random_prime():
    primes = [i for i in range(1, 500) if isprime(i)]
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
    t, newt = 0, 1
    r, newr = phi_n, e
    while newr != 0:
        q = r // newr
        t, newt = newt, t - q * newt
        r, newr = newr, r - q * newr
    if t < 0:
        t = t + phi_n
    return t


d = get_d(e, phi_n)
print("Private key are [ d = {} and n = {} ]".format(d, n))


# Encryption : c = m^e mod n

def encrypt(plain_text):
    # ord =  Return the Unicode code point for a one-character string
    cipher_text = [ord(x) ** e % n for x in plain_text]
    return cipher_text


plain_text = input("Please enter text to encrypt : ")
cipher_text = encrypt(plain_text)
print("Encryption of {} is {}".format(plain_text, cipher_text))


# Decryption : m = c^d mod n

def decrypt(cipher_text):
    decoded_text = ''.join([chr(x ** d % n) for x in cipher_text])
    return decoded_text


message = decrypt(cipher_text)
print("Decryption of {} is {}".format(cipher_text, message))
