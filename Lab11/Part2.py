import random

def find_points_on_curve(modulus=23):
    """
    Finds all points (x, y) that satisfy the elliptic curve equation:
    y^2 = (x^3 + x + 1) mod modulus

    Parameters:
        modulus (int): The modulus to use in the equation.

    Returns:
        list: A list of tuples representing the points (x, y) on the curve.
    """
    points = []  # List to store the valid points

    # Iterate over all possible values of x in the range [0, modulus - 1]
    for x in range(modulus):
        # Compute the right-hand side of the equation: (x^3 + x + 1) % modulus
        rhs = (x**3 + x + 1) % modulus

        # Iterate over all possible values of y in the range [0, modulus - 1]
        for y in range(modulus):
            # Compute the left-hand side of the equation: y^2 % modulus
            lhs = (y**2) % modulus

            # Check if lhs equals rhs (y^2 == x^3 + x + 1 mod modulus)
            if lhs == rhs:
                points.append((x, y))  # Add the valid point (x, y) to the list

    return points

def point_addition(P, Q, a, p):
    """
    Adds two points P and Q on the elliptic curve y^2 = x^3 + ax + b mod p.

    Parameters:
        P (tuple): The first point (x1, y1).
        Q (tuple): The second point (x2, y2).
        a (int): The coefficient of x in the curve equation.
        p (int): The modulus.

    Returns:
        tuple: The resulting point (x3, y3).
    """
    if P is None:
        return Q
    if Q is None:
        return P

    x1, y1 = P
    x2, y2 = Q

    if P == Q:
        # Point doubling
        m = (3 * x1**2 + a) * pow(2 * y1, -1, p) % p
    else:
        # Point addition
        if x1 == x2 and y1 != y2:
            return None  # P + (-P) = O
        m = (y2 - y1) * pow(x2 - x1, -1, p) % p

    x3 = (m**2 - x1 - x2) % p
    y3 = (m * (x1 - x3) - y1) % p
    return x3, y3

def scalar_multiplication(k, P, a, p):
    """
    Multiplies a point P by a scalar k on the elliptic curve.

    Parameters:
        k (int): The scalar multiplier.
        P (tuple): The point (x, y) to multiply.
        a (int): The coefficient of x in the curve equation.
        p (int): The modulus.

    Returns:
        tuple: The resulting point after scalar multiplication.
    """
    result = None  # Start with the identity element
    addend = P

    while k:
        if k & 1:
            result = point_addition(result, addend, a, p)
        addend = point_addition(addend, addend, a, p)
        k >>= 1

    return result

def elgamal_encrypt(Pm, G, public_key, a, p):
    """
    Encrypts a message point using the El-Gamal cryptosystem.

    Parameters:
        Pm (tuple): The plaintext point (x, y).
        G (tuple): The base point (generator).
        public_key (tuple): The public key point.
        a (int): The coefficient of x in the curve equation.
        p (int): The modulus.

    Returns:
        tuple: The ciphertext (C1, C2).
    """
    k = random.randint(1, p - 1)  # Random ephemeral key
    C1 = scalar_multiplication(k, G, a, p)
    C2 = point_addition(Pm, scalar_multiplication(k, public_key, a, p), a, p)
    return C1, C2

def elgamal_decrypt(C1, C2, private_key, a, p):
    """
    Decrypts a ciphertext using the El-Gamal cryptosystem.

    Parameters:
        C1 (tuple): The first part of the ciphertext.
        C2 (tuple): The second part of the ciphertext.
        private_key (int): The private key scalar.
        a (int): The coefficient of x in the curve equation.
        p (int): The modulus.

    Returns:
        tuple: The decrypted plaintext point (x, y).
    """
    S = scalar_multiplication(private_key, C1, a, p)
    if S is None:
        raise ValueError("Scalar multiplication resulted in None. Check input parameters.")
    S_neg = (S[0], -S[1] % p)  # Negate the y-coordinate
    Pm = point_addition(C2, S_neg, a, p)
    return Pm

# Testing the El-Gamal cryptosystem
if __name__ == "__main__":
    # Curve parameters
    p = 23
    a, b = 1, 1
    G = (17, 20)  # Base point

    # Key generation
    private_key = random.randint(1, p - 1)
    public_key = scalar_multiplication(private_key, G, a, p)

    print(f"Private key: {private_key}")
    print(f"Public key: {public_key}")

    # Encrypt a message point (example point from the curve)
    Pm = (5, 19)
    print(f"Plaintext point: {Pm}")

    C1, C2 = elgamal_encrypt(Pm, G, public_key, a, p)
    print(f"Ciphertext: (C1={C1}, C2={C2})")

    # Decrypt the ciphertext
    try:
        decrypted_point = elgamal_decrypt(C1, C2, private_key, a, p)
        print(f"Decrypted point: {decrypted_point}")
    except ValueError as e:
        print(f"Decryption error: {e}")
