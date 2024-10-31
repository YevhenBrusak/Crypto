def inverse_element_2(a, p):
    # Застосовуємо малу теорему Ферма для обчислення оберненого елемента
    if a % p == 0:
        return None  # Обернений елемент не існує, якщо a кратне p
    return pow(a, p - 2, p)  # Обчислюємо a^(p-2) mod p

# Тестування функції на прикладі a = 5 і n = 18
a = 3
n = 7

# Перевіряємо, чи n є простим числом
from sympy import isprime
if isprime(n):
    inverse = inverse_element_2(a, n)
    if inverse is not None:
        print(f"Мультиплікативний обернений елемент для {a} модуль {n}: {inverse}")
    else:
        print(f"Мультиплікативного оберненого елемента для {a} модуль {n} не існує.")
else:
    print(f"Число {n} не є простим, тому мала теорема Ферма не застосовується.")