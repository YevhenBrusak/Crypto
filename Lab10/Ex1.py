import struct
import math

# Константи для MD5
S = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
     5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

# Обчислюємо таблицю K (константи, отримані з синусів)
K = [int(abs(math.sin(i + 1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

# Функція для лівого циклічного зсуву
def left_rotate(x, amount):
    """Лівий циклічний зсув 32-бітного числа."""
    x &= 0xFFFFFFFF
    return ((x << amount) | (x >> (32 - amount))) & 0xFFFFFFFF

# Реалізація MD5
def md5(message):
    """Реалізація MD5-хешування."""
    # Крок 1: Додавання доповнення до повідомлення (padding)
    original_length_bits = (len(message) * 8) & 0xFFFFFFFFFFFFFFFF
    message += b'\x80'  # Додаємо одиничний біт і заповнюємо нулями
    while (len(message) * 8) % 512 != 448:
        message += b'\x00'
    # Додаємо довжину початкового повідомлення (64 біти)
    message += struct.pack('<Q', original_length_bits)

    # Крок 2: Ініціалізація буферів MD5
    A, B, C, D = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476

    # Крок 3: Розбиваємо повідомлення на 512-бітні блоки
    for chunk_offset in range(0, len(message), 64):
        chunk = message[chunk_offset:chunk_offset + 64]
        M = struct.unpack('<' + 'I'*16, chunk)  # Розбиваємо блок на 16 слів
        a, b, c, d = A, B, C, D

        # Основний цикл MD5 (64 ітерації)
        for i in range(64):
            if i < 16:
                f = (b & c) | (~b & d)
                g = i
            elif i < 32:
                f = (d & b) | (~d & c)
                g = (5 * i + 1) % 16
            elif i < 48:
                f = b ^ c ^ d
                g = (3 * i + 5) % 16
            else:
                f = c ^ (b | ~d)
                g = (7 * i) % 16

            f = (f + a + K[i] + M[g]) & 0xFFFFFFFF
            a, d, c, b = d, c, b, (b + left_rotate(f, S[i])) & 0xFFFFFFFF

        # Додаємо результат блоку до поточних значень
        A = (A + a) & 0xFFFFFFFF
        B = (B + b) & 0xFFFFFFFF
        C = (C + c) & 0xFFFFFFFF
        D = (D + d) & 0xFFFFFFFF

    # Крок 4: Формуємо фінальний хеш (128 біт)
    return struct.pack('<4I', A, B, C, D).hex()

# Приклад використання
if __name__ == "__main__":
    test_message = b"I am Iron Man"  # Повідомлення для хешування
    print(f"MD5('{test_message.decode()}') = {md5(test_message)}")
