"""Educational RSA digital signatures."""

import hashlib
import math
import secrets


def _is_prime(n: int, rounds: int = 12) -> bool:
	"""Probabilistic primality test using Miller-Rabin."""
	if n < 2:
		return False
	for prime in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
		if n == prime:
			return True
		if n % prime == 0:
			return False

	d, s = n - 1, 0
	while d % 2 == 0:
		d //= 2
		s += 1

	for _ in range(rounds):
		a = secrets.randbelow(n - 3) + 2
		x = pow(a, d, n)
		if x in (1, n - 1):
			continue
		for _ in range(s - 1):
			x = pow(x, 2, n)
			if x == n - 1:
				break
		else:
			return False
	return True


def _prime(bits: int) -> int:
	while True:
		candidate = secrets.randbits(bits) | (1 << (bits - 1)) | 1
		if _is_prime(candidate):
			return candidate


def generate_keys(bits: int = 512) -> tuple[tuple[int, int], tuple[int, int]]:
	"""Return (public_key, private_key), with keys represented as (exponent, n)."""
	if bits < 64:
		raise ValueError("bits must be at least 64")
	e = 65537
	while True:
		p, q = _prime(bits // 2), _prime(bits // 2)
		if p == q:
			continue
		n = p * q
		phi = (p - 1) * (q - 1)
		if math.gcd(e, phi) == 1:
			d = pow(e, -1, phi)
			return (e, n), (d, n)


def _hash(message: bytes) -> int:
	return int.from_bytes(hashlib.sha256(message).digest(), "big")


def sign(message: bytes, private_key: tuple[int, int]) -> int:
	"""Sign bytes with the RSA private key."""
	d, n = private_key
	digest = _hash(message)
	if digest >= n:
		raise ValueError("RSA modulus is too small for SHA-256")
	return pow(digest, d, n)


def verify(message: bytes, signature: int, public_key: tuple[int, int]) -> bool:
	"""Verify an RSA signature against bytes."""
	e, n = public_key
	return 0 <= signature < n and pow(signature, e, n) == _hash(message)


if __name__ == "__main__":
	public_key, private_key = generate_keys()
	message = b"RSA digital signatures"
	signature = sign(message, private_key)
	print("Valid:", verify(message, signature, public_key))
	print("Tampered:", verify(message + b"!", signature, public_key))
