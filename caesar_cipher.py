# Python3.6  
# Coding: utf-8  

def get_double_alphabet(alphabet:str):
    double_alphabet = alphabet + alphabet
    return double_alphabet
    # print(double_alphabet)


def get_message():
    string_to_encrypt = input("Please enter a message to encrypt: ")
    return string_to_encrypt
    # print(string_to_encrypt)


def get_cipher_key():
    shift_amount = input("Please enter a key (whole number from 1-25): ")
    return shift_amount
    # print(shift_amount)
    


def encrypt_message(message:str, cipher_key:int, alphabet:str):
    encypted_message = ""
    upper_case_message = ""
    upper_case_message = message.upper()
    for current_character in upper_case_message:
        position = alphabet.find(current_character)
        new_position = position + int(cipher_key)
        if current_character in alphabet:
            encypted_message = encypted_message + alphabet[new_position]
        else:
            encypted_message = encypted_message + current_character
    return encypted_message


def decrypt_message(message, cipher_key, alphabet):
    decrypt_key = -1 * int(cipher_key)
    return encrypt_message(message, decrypt_key, alphabet)


# Creating a main function
def run_caesar_cipher_program():
    my_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alphabet: {my_alphabet}')
    my_alphabet2 = get_double_alphabet(my_alphabet)
    print(f'Alphabet2: {my_alphabet2}')
    my_message = get_message()
    print(my_message)
    my_cipher_key = get_cipher_key()
    print(my_cipher_key)
    my_encrypted_message = encrypt_message(my_message, my_cipher_key, my_alphabet2)
    print(f'Encrypted Message: {my_encrypted_message}')
    my_decrypted_message = decrypt_message(my_encrypted_message, my_cipher_key, my_alphabet2)
    print(f'Decypted Message: {my_decrypted_message}')


run_caesar_cipher_program()