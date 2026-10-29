"""A small, educational elliptic-curve cryptography implementation.

This demonstrates point arithmetic and ECDH key agreement over a prime field.
It is not suitable for protecting real data; use a vetted cryptographic
library (for example, ``cryptography``) in production.
"""

from dataclasses import dataclass
import secrets


@dataclass(frozen=True)
class Point:
	"""A point on y² = x³ + a*x + b, or the point at infinity (None, None)."""

	x: int | None
	y: int | None

	@property
	def infinity(self) -> bool:
		return self.x is None and self.y is None


INFINITY = Point(None, None)


class EllipticCurve:
	def __init__(self, a: int, b: int, prime: int, generator: Point, order: int):
		if (4 * a**3 + 27 * b**2) % prime == 0:
			raise ValueError("The curve is singular")
		self.a, self.b, self.p = a % prime, b % prime, prime
		self.generator, self.order = generator, order
		if not self.is_on_curve(generator):
			raise ValueError("The generator is not on the curve")

	def is_on_curve(self, point: Point) -> bool:
		if point.infinity:
			return True
		return (point.y * point.y - point.x**3 - self.a * point.x - self.b) % self.p == 0

	def add(self, left: Point, right: Point) -> Point:
		if not self.is_on_curve(left) or not self.is_on_curve(right):
			raise ValueError("Point is not on this curve")
		if left.infinity:
			return right
		if right.infinity:
			return left
		if left.x == right.x and (left.y + right.y) % self.p == 0:
			return INFINITY

		if left == right:
			if left.y % self.p == 0:
				return INFINITY
			slope = ((3 * left.x * left.x + self.a) * pow(2 * left.y, -1, self.p)) % self.p
		else:
			slope = ((right.y - left.y) * pow(right.x - left.x, -1, self.p)) % self.p

		x = (slope * slope - left.x - right.x) % self.p
		y = (slope * (left.x - x) - left.y) % self.p
		return Point(x, y)

	def multiply(self, scalar: int, point: Point | None = None) -> Point:
		"""Compute scalar * point using double-and-add."""
		if point is None:
			point = self.generator
		if scalar < 0:
			raise ValueError("Scalar must be non-negative")
		result = INFINITY
		addend = point
		while scalar:
			if scalar & 1:
				result = self.add(result, addend)
			addend = self.add(addend, addend)
			scalar >>= 1
		return result

	def generate_key_pair(self) -> tuple[int, Point]:
		private = secrets.randbelow(self.order - 1) + 1
		return private, self.multiply(private)

	def shared_secret(self, private_key: int, public_key: Point) -> Point:
		if not self.is_on_curve(public_key):
			raise ValueError("Public key is not on this curve")
		return self.multiply(private_key, public_key)


# Small, deliberately readable example parameters (not secure parameters).
CURVE = EllipticCurve(a=2, b=3, prime=97, generator=Point(3, 6), order=5)


if __name__ == "__main__":
	alice_private, alice_public = CURVE.generate_key_pair()
	bob_private, bob_public = CURVE.generate_key_pair()
	alice_secret = CURVE.shared_secret(alice_private, bob_public)
	bob_secret = CURVE.shared_secret(bob_private, alice_public)
	assert alice_secret == bob_secret
	print("Alice public key:", alice_public)
	print("Bob public key:  ", bob_public)
	print("Shared secret:   ", alice_secret)
