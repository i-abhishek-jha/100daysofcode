# Caesar Cipher using two Function
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(original_text, shift_amount):
    decoded_string = ""

    for letter in original_text:
        if letter in alphabet:
            original_pos = alphabet.index(letter)
            decoded_pos = (original_pos - shift_amount) % 26
            decoded_string += alphabet[decoded_pos]
        else:
            decoded_string += letter

    print(decoded_string)

def encrypt(original_text, shift_amount):
    encoded_string = ""

    for letter in original_text:
        if letter in alphabet:
            original_pos = alphabet.index(letter)
            encoded_pos = (original_pos + shift_amount) % 26
            encoded_string += alphabet[encoded_pos]
        else:
            encoded_string += letter

    print(encoded_string)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Invalid direction!")