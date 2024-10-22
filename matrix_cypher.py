import numpy as np

# Функція для створення порядку індексів на основі ключа
def generate_key_order(key):
    # Створення списку індексів ключа
    indices = list(range(len(key)))
    # Сортування індексів відповідно до значень символів ключа
    sorted_indices = sorted(indices, key=lambda index: key[index])
    return sorted_indices

# Функція для створення зворотного порядку індексів для перестановки
def generate_inverse_key_order(order):
    # Ініціалізація списку того ж розміру, що й порядок, заповнений нулями
    inverse_order = [0] * len(order)
    # Для кожної позиції у вихідному порядку заповнюється зворотний порядок
    for i, pos in enumerate(order):
        inverse_order[pos] = i
    return inverse_order

# Функція шифрування повідомлення з використанням двох ключів (рядковий та стовпчиковий)
def encrypt_with_two_keys(message, row_key, col_key):
    # Генерування порядків перестановки для рядків і стовпців
    row_order = generate_key_order(row_key)
    col_order = generate_key_order(col_key)
    
    message = message.replace(" ", "")
    matrix_size = len(row_key) * len(col_key)
    # Обчислення кількості додаткових символів для заповнення матриці
    padding = matrix_size - len(message)
    message += " " * padding
    
    matrix = np.array(list(message)).reshape(len(row_key), len(col_key))
    
    # Перестановка рядків відповідно до порядку row_order
    row_permuted = matrix[row_order]
    
    # Перестановка стовпців відповідно до порядку col_order
    final_matrix = row_permuted[:, col_order]
    
    # Перетворення фінальної матриці у рядок для отримання зашифрованого повідомлення
    encrypted_message = ''.join(final_matrix.flatten())
    return encrypted_message

# Функція розшифрування повідомлення з використанням двох ключів
def decrypt_with_two_keys(encrypted_message, row_key, col_key):
    row_order = generate_key_order(row_key)
    col_order = generate_key_order(col_key)
    
    inverse_row_order = generate_inverse_key_order(row_order)
    inverse_col_order = generate_inverse_key_order(col_order)
    
    matrix = np.array(list(encrypted_message)).reshape(len(row_key), len(col_key))
    
    col_permuted = matrix[:, inverse_col_order]
    
    original_matrix = col_permuted[inverse_row_order]
    
    decrypted_message = ''.join(original_matrix.flatten()).strip()
    return decrypted_message

# Приклад використання
message = "халамадрід"
row_key = "шифр"
col_key = "крипто"

encrypted_message = encrypt_with_two_keys(message, row_key, col_key)
print(f"Encrypted message: {encrypted_message}")

decrypted_message = decrypt_with_two_keys(encrypted_message, row_key, col_key)
print(f"Decrypted message: {decrypted_message}")