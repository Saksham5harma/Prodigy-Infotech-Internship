#Ceasar Cipher Implementation
import string

def caesar_cipher(text, shift):

    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + shift - 97) % 26 + 97)

    return result
text = input("Enter Message: ")
shift =int(input("Enter Shift Key: "))

encrypted_text = caesar_cipher(text, shift)
print("Encrypted text: ", encrypted_text)

decrypted_text = caesar_cipher(encrypted_text, -shift)
print("Decrypted text: ", decrypted_text)
