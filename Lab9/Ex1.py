import random

# Miller-Rabin primality test
def is_prime(n, k=5):
    """Перевіряє, чи є число простим за допомогою тесту Міллера-Рабіна."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

# Generate a large prime number
def generate_large_prime(bits=512):
    """Генерує велике просте число заданої довжини."""
    while True:
        candidate = random.getrandbits(bits)
        candidate |= (1 << (bits - 1)) | 1
        if is_prime(candidate):
            return candidate

# Find a primitive root modulo p
def find_primitive_root(p):
    """Знаходить примітивний корінь для модуля p."""
    if p == 2:
        return 1
    p1, p2 = 2, (p - 1) // 2
    for g in range(2, p):
        if pow(g, (p - 1) // p1, p) != 1 and pow(g, (p - 1) // p2, p) != 1:
            return g
    return None

# El-Gamal Key Generation
def elgamal_key_generation(bits=512):
    """Генерує відкриті та закриті ключі El-Gamal."""
    p = generate_large_prime(bits)
    g = find_primitive_root(p)
    private_key = random.randint(2, p - 2)
    public_key = pow(g, private_key, p)
    return (p, g, public_key), private_key

# El-Gamal Encryption
def elgamal_encrypt(message, public_key):
    """Шифрує повідомлення за допомогою алгоритму El-Gamal."""
    p, g, y = public_key
    k = random.randint(2, p - 2)
    c1 = pow(g, k, p)
    c2 = (message * pow(y, k, p)) % p
    return c1, c2

# El-Gamal Decryption
def elgamal_decrypt(ciphertext, private_key, p):
    """Розшифровує повідомлення за допомогою алгоритму El-Gamal."""
    c1, c2 = ciphertext
    s = pow(c1, private_key, p)
    s_inv = pow(s, -1, p)  # Modular multiplicative inverse
    decrypted_message = (c2 * s_inv) % p
    return decrypted_message

# Example Usage
if __name__ == "__main__":
    # Generate keys
    public_key, private_key = elgamal_key_generation(bits=512)
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Encrypt a message
    message = 3457  # Example plaintext message
    ciphertext = elgamal_encrypt(message, public_key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the message
    decrypted_message = elgamal_decrypt(ciphertext, private_key, public_key[0])
    print(f"Decrypted Message: {decrypted_message}")

    # Verify the decryption
    assert message == decrypted_message, "Decryption failed!"
    print("Encryption and Decryption are successful!")