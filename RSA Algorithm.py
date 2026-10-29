"""A small educational implementation of the RSA algorithm.

This demonstrates RSA key generation, encryption, and decryption for small
messages.  It is not intended for production cryptography.
"""

from math import gcd
from secrets import randbelow


def is_prime(number: int) -> bool:
    """Return whether *number* is prime."""
    if number < 2:
        return False
    if number % 2 == 0:
        return number == 2
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True


def modular_inverse(value: int, modulus: int) -> int:
    """Return the multiplicative inverse of value modulo modulus."""
    old_r, r = value, modulus
    old_s, s = 1, 0
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
    if old_r != 1:
        raise ValueError("The modular inverse does not exist.")
    return old_s % modulus


def generate_keys(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Generate and return ((public exponent, n), (private exponent, n))."""
    if p == q or not is_prime(p) or not is_prime(q):
        raise ValueError("p and q must be distinct prime numbers.")

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537 if gcd(65537, phi) == 1 else 3
    while gcd(e, phi) != 1:
        e = 2 + randbelow(phi - 2)
    d = modular_inverse(e, phi)
    return (e, n), (d, n)


def encrypt(message: str, public_key: tuple[int, int]) -> list[int]:
    """Encrypt a string as a list of RSA ciphertext integers."""
    exponent, modulus = public_key
    if any(ord(character) >= modulus for character in message):
        raise ValueError("Each character must have a value smaller than n.")
    return [pow(ord(character), exponent, modulus) for character in message]


def decrypt(ciphertext: list[int], private_key: tuple[int, int]) -> str:
    """Decrypt a list of RSA ciphertext integers into a string."""
    exponent, modulus = private_key
    return "".join(chr(pow(value, exponent, modulus)) for value in ciphertext)


if __name__ == "__main__":
    public_key, private_key = generate_keys(61, 53)
    message = "RSA works!"
    encrypted = encrypt(message, public_key)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypt(encrypted, private_key))