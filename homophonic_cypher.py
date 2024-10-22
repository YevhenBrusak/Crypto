import random

# Таблиця гомофонів для української мови
homophonic_table = {
    'А': ['11', '12', '13'],
    'Б': ['21', '22'],
    'В': ['31', '32', '33'],
    'Г': ['41', '42'],
    'Д': ['51', '52', '53'],
    'Е': ['61', '62'],
    'Є': ['71'],
    'Ж': ['81'],
    'З': ['91', '92'],
    'И': ['101', '102'],
    'І': ['111', '112'],
    'Ї': ['121'],
    'Й': ['131'],
    'К': ['141', '142'],
    'Л': ['151', '152', '153'],
    'М': ['161', '162'],
    'Н': ['171', '172', '173'],
    'О': ['181', '182', '183', '184'],
    'П': ['191', '192'],
    'Р': ['201', '202', '203'],
    'С': ['211', '212', '213'],
    'Т': ['221', '222', '223'],
    'У': ['231', '232'],
    'Ф': ['241'],
    'Х': ['251'],
    'Ц': ['261'],
    'Ч': ['271'],
    'Ш': ['281'],
    'Щ': ['291'],
    'Ь': ['301'],
    'Ю': ['311'],
    'Я': ['321']
}

# Функція для шифрування
def homophonic_encrypt(text):
    encrypted_text = []
    for char in text.upper():
        if char in homophonic_table:
            encrypted_text.append(random.choice(homophonic_table[char]))
        else:
            encrypted_text.append(char)  # Не шифруємо неалфавітні символи
    return ' '.join(encrypted_text)

# Функція для розшифрування
def homophonic_decrypt(encrypted_text):
    decrypted_text = []
    encrypted_list = encrypted_text.split()
    
    # Перевертаємо таблицю для пошуку за значенням
    reverse_table = {hom: letter for letter, homophones in homophonic_table.items() for hom in homophones}
    
    for code in encrypted_list:
        if code in reverse_table:
            decrypted_text.append(reverse_table[code])
        else:
            decrypted_text.append(code)
    
    return ''.join(decrypted_text)

# Приклад використання
text = "Сонцестояння"
encrypted = homophonic_encrypt(text)
decrypted = homophonic_decrypt(encrypted)

print("Оригінальний текст:", text)
print("Зашифрований текст:", encrypted)
print("Розшифрований текст:", decrypted)