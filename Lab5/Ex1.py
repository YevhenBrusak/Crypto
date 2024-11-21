import random

def miller_rabin(p, k):
    # Базові перевірки
    if p <= 1 or p % 2 == 0:
        return "Composite"
    
    # Представляємо p-1 у вигляді 2^s * d
    s, d = 0, p - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    # Функція для перевірки свідка
    def is_composite(a):
        """
        Допоміжна функція для перевірки, чи є a свідком того, що p є складеним.
        """
        x = pow(a, d, p)  # a^d mod p
        if x == 1 or x == p - 1:
            return False  # Число, можливо, просте
        for _ in range(s - 1):
            x = pow(x, 2, p)
            if x == p - 1:
                return False  # Число, можливо, просте
        return True  # Свідок знайшов, що число складене

    # Запускаємо k раундів перевірки
    for _ in range(k):
        a = random.randint(2, p - 2)  # Випадкове число у діапазоні [2, p-2]
        if is_composite(a):
            return "Composite"  # Число точно складене

    # Якщо всі раунди пройдено
    probability = 1 - (1 / (2 ** k))  # Ймовірність, що число просте
    return f"Probably Prime with probability {probability:.5f}"


# Тест
p = 57
k = 5
result = miller_rabin(p, k)
print(f"Number {p}: {result}")

p = 83
result = miller_rabin(p, k)
print(f"Number {p}: {result}")