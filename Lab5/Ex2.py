import random

# Функція для перевірки простоти числа за допомогою тесту Міллера-Рабіна
def is_prime(n, k=5):  # k - кількість раундів перевірки
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Представлення n-1 у вигляді 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Проведення k раундів тесту
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

# Генерація великого простого числа (~1024 біт)
def generate_large_prime(bits=1024):
    while True:
        candidate = random.getrandbits(bits) | (1 << bits - 1) | 1  # забезпечення непарності та потрібної довжини
        if is_prime(candidate):
            return candidate

# Розширений алгоритм Евкліда для знаходження оберненого числа
def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

# Генерація ключів RSA
def generate_keys():
    # Крок 1: Генерація простих чисел p і q
    p = generate_large_prime()
    q = generate_large_prime()
    n = p * q
    phi = (p - 1) * (q - 1)

    # Крок 2: Вибір відкритого ключа e
    e = 65537  # стандартне значення e
    gcd, d, _ = gcd_extended(e, phi)
    while gcd != 1:  # забезпечення взаємної простоти з φ(n)
        e = random.randrange(2, phi)
        gcd, d, _ = gcd_extended(e, phi)

    # Крок 3: Визначення секретного ключа d
    d = d % phi
    if d < 0:
        d += phi

    return ((e, n), (d, n))

# Шифрування повідомлення
def encrypt(message, public_key):
    e, n = public_key
    return [pow(ord(char), e, n) for char in message]

# Розшифрування повідомлення
def decrypt(ciphertext, private_key):
    d, n = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Головна частина програми
if __name__ == "__main__":
    print("Генерація ключів RSA...")
    public_key, private_key = generate_keys()
    print(f"Відкритий ключ: {public_key}")
    print(f"Секретний ключ: {private_key}")

    # Тест
    message = "Hello, RSA!"
    print(f"Повідомлення: {message}")

    encrypted = encrypt(message, public_key)
    print(f"Зашифроване повідомлення: {encrypted}")

    decrypted = decrypt(encrypted, private_key)
    print(f"Розшифроване повідомлення: {decrypted}")