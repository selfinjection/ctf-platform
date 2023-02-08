def decrypt_caesar(ciphertext, shift):
    result = ''
    for char in ciphertext:
        if char.isalpha():
            char = chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
        result += char
    return result

def main():
    ciphertext = "GUVF VF ZL FRPERG ZRFFNTR."
    plaintext = decrypt_caesar(ciphertext, 13)
    print(f'The decrypted message is: {plaintext}')

main()