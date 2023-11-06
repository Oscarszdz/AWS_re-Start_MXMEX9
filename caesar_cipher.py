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
    myMessage = get_message()
    print(myMessage)
    myCipherKey = get_cipher_key()
    print(myCipherKey)
    myEncryptedMessage = encrypt_message(myMessage, myCipherKey, my_alphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    myDecryptedMessage = decrypt_message(myEncryptedMessage, myCipherKey, my_alphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


run_caesar_cipher_program()