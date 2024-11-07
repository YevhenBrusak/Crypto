ip_table = [ 58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7 ]
pc1_table = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]
shift_schedule = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
pc2_table = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]
e_box_table = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]
s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]
p_box_table = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]
ip_inverse_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]
# Перетворення рядка в двійкове значення
def string_to_binary(input_string):
    binary_output = ''.join(format(ord(char), '08b') for char in input_string)
    return binary_output[:64].ljust(64, '0')
# Перетворення рядка в ASCII
def binary_to_ascii(binary_string):
    ascii_output = ''.join(chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8))
    return ascii_output
# Початкова перестановка в двійковому значенні
def apply_ip(binary_input):
    permuted = ''.join(binary_input[ip_table[i] - 1] for i in range(64))
    return permuted
# Ключ в двійковому значенні
def convert_key_to_binary():
    key = 'abcdefgh'
    return ''.join(format(ord(c), '08b') for c in key)
# Генерація ключів для алгоритму DES
def generate_round_keys():
    key_binary = convert_key_to_binary()
    key_pc1 = ''.join(key_binary[bit - 1] for bit in pc1_table)
    # Поділ на ліву та праву частини
    left_half = key_pc1[:28]
    right_half = key_pc1[28:]
    round_keys = []
    
    for shift in shift_schedule:
        left_half = left_half[shift:] + left_half[:shift]
        right_half = right_half[shift:] + right_half[:shift]  
        # Об'єднання та застосування PC2
        combined = left_half + right_half
        round_key = ''.join(combined[pc2_table[i] - 1] for i in range(48))
        round_keys.append(round_key)
    return round_keys
#Шифрування
def encryption(user_input):
    binary_rep_of_input = string_to_binary(user_input)
    # Ініціалізація списків для зберігання ключів
    round_keys = generate_round_keys()
    ip_result_str = apply_ip(binary_rep_of_input)
    # Початковий результат перестановки ділиться на 2 половини
    lpt = ip_result_str[:32]
    rpt = ip_result_str[32:]
    for round_num in range(16):
        # 32 бітів в 48 бітів
        expanded_result = [rpt[i - 1] for i in e_box_table]
        # Перетворення результату назад у рядок для кращої візуалізації
        expanded_result_str = ''.join(expanded_result)
        # Ключ для даного рядка
        round_key_str = round_keys[round_num]
        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))

        # Розбиття 48-бітних рядків на 8 груп по 6 біт у кожній
        six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]
        s_box_substituted = ''

        # Застосування заміни S-box для кожної 6-бітової групи
        for i in range(8):
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)
            s_box_value = s_boxes[i][row_bits][col_bits]
            s_box_substituted += format(s_box_value, '04b')
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]
        # Перетворення LPT у список бітів для операції XOR
        lpt_list = list(lpt)
        # XOR
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]
        new_rpt_str = ''.join(new_rpt)
        lpt = rpt
        rpt = new_rpt_str

    final_result = rpt + lpt
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]
    final_cipher_str = ''.join(final_cipher)
    print("Final Cipher binary:", final_cipher_str)

    final_cipher_ascii = binary_to_ascii(final_cipher_str)
    return final_cipher_ascii

# Розшифрування
def decryption(final_cipher):

    round_keys = generate_round_keys()
    ip_dec_result_str = apply_ip(final_cipher)
    lpt = ip_dec_result_str[:32]
    rpt = ip_dec_result_str[32:]

    for round_num in range(16):
        expanded_result = [rpt[i - 1] for i in e_box_table]
        expanded_result_str = ''.join(expanded_result)
        round_key_str = round_keys[15-round_num]
        xor_result_str = ''
        for i in range(48):
            xor_result_str += str(int(expanded_result_str[i]) ^ int(round_key_str[i]))
    
        # Розбиття 48-бітний рядків на 8 груп по 6 біт у кожній
        six_bit_groups = [xor_result_str[i:i+6] for i in range(0, 48, 6)]
        s_box_substituted = ''
        for i in range(8):
            row_bits = int(six_bit_groups[i][0] + six_bit_groups[i][-1], 2)
            col_bits = int(six_bit_groups[i][1:-1], 2)
            s_box_value = s_boxes[i][row_bits][col_bits] 
            s_box_substituted += format(s_box_value, '04b')
    
        p_box_result = [s_box_substituted[i - 1] for i in p_box_table]    
        lpt_list = list(lpt)
        new_rpt = [str(int(lpt_list[i]) ^ int(p_box_result[i])) for i in range(32)]
        new_rpt_str = ''.join(new_rpt)
        lpt = rpt
        rpt = new_rpt_str
    final_result = rpt + lpt
    final_cipher = [final_result[ip_inverse_table[i] - 1] for i in range(64)]
    final_cipher_str = ''.join(final_cipher)
    final_cipher_ascii = binary_to_ascii(final_cipher_str)
    print("Decryption of Cipher :", final_cipher_ascii)
    return final_cipher_ascii

# Робота програми
user_input = input("Enter a string: ")

enc = encryption(user_input)

enc_to_binary = string_to_binary(enc)

dec = decryption(enc_to_binary)