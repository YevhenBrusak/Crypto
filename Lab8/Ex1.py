import random

def is_prime(n, k=5):
    """
    Перевірка простоти числа n за допомогою тесту Міллера-Рабіна.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Представляємо n-1 у вигляді 2^r * d
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

# Генерація безпечного простого p (p = 2q + 1, де q теж просте)
def generate_safe_prime(bits=512):
    while True:
        q = random.getrandbits(bits - 1)
        q |= (1 << (bits - 2)) | 1  # q непарне та має правильну довжину біта
        if is_prime(q):
            p = 2 * q + 1
            if is_prime(p):
                return p

def find_primitive_root(p):
    """
    Знаходження примітивного кореня (генератора) для модуля p.
    """
    q = (p - 1) // 2  # q - простий множник p-1
    for g in range(2, p):
        # Перевіряємо, чи g є генератором
        if pow(g, 2, p) != 1 and pow(g, q, p) != 1:
            return g

# Обмін ключами по протоколу Діффі-Хелмана
def diffie_hellman_key_exchange():
    print("Генерація безпечного простого числа p...")
    p = generate_safe_prime(bits=512)
    print(f"Safe prime p: {p}")

    print("Знаходження примітивного кореня g...")
    g = find_primitive_root(p)
    print(f"Primitive root g: {g}")

    # Приватні та публічні ключі Аліси
    a_private = random.randint(2, p - 2)
    a_public = pow(g, a_private, p)

    # Приватні та публічні ключі Боба
    b_private = random.randint(2, p - 2)
    b_public = pow(g, b_private, p)

    print(f"Alice's public key: {a_public}")
    print(f"Bob's public key: {b_public}")

    alice_shared_secret = pow(b_public, a_private, p)
    bob_shared_secret = pow(a_public, b_private, p)

    print(f"Alice's shared secret: {alice_shared_secret}")
    print(f"Bob's shared secret: {bob_shared_secret}")

    if alice_shared_secret == bob_shared_secret:
        print("Успішний обмін ключами!")
    else:
        print("Помилка в обміні ключами!")

diffie_hellman_key_exchange()