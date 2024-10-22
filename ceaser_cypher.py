def generate_cipher_alphabet(alphabet, key, keyword):
    # Унікальні символи ключового слова (видаляємо дублікати, зберігаючи порядок)
    keyword_unique = "".join(sorted(set(keyword), key=keyword.index))
    
    # Створюємо початковий алфавіт з початком з ключа
    shifted_alphabet = alphabet[key:] + alphabet[:key]
    
    # Видаляємо символи ключового слова з алфавіту
    for char in keyword_unique:
        shifted_alphabet = shifted_alphabet.replace(char, "")
    
    # Вставляємо ключове слово на позицію з індексом key
    cipher_alphabet = shifted_alphabet[:key] + keyword_unique + shifted_alphabet[key:]
    
    print(f"Алфавіт: {cipher_alphabet}")
    return cipher_alphabet

def caesar_cipher_encrypt(text, alphabet, key, keyword):
    # Генеруємо шифрувальний алфавіт
    cipher_alphabet = generate_cipher_alphabet(alphabet, key, keyword)
    encrypted_text = ""
    
    # Шифруємо кожен символ
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_text += cipher_alphabet[index]
        else:
            encrypted_text += char  # якщо символ не в алфавіті, не шифруємо
    
    return encrypted_text

def caesar_cipher_decrypt(text, alphabet, key, keyword):
    # Генеруємо шифрувальний алфавіт для розшифрування
    cipher_alphabet = generate_cipher_alphabet(alphabet, key, keyword)
    decrypted_text = ""
    
    # Дешифруємо кожен символ
    for char in text:
        if char in cipher_alphabet:
            index = cipher_alphabet.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char  # якщо символ не в алфавіті, не дешифруємо
    
    return decrypted_text

# Приклад використання
alphabet = "АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦШЩЬЮЯ"
key = 3
keyword = "ПРОГРАМНЕ"
text_to_encrypt = "ЗАБЕЗПЕЧЕННЯ"

encrypted = caesar_cipher_encrypt(text_to_encrypt, alphabet, key, keyword)
decrypted = caesar_cipher_decrypt(encrypted, alphabet, key, keyword)

print(f"Зашифрований текст: {encrypted}")
print(f"Розшифрований текст: {decrypted}")
