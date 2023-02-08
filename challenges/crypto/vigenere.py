def vigenere_cipher(ciphertext, key, encrypt=True):
    plaintext = ""
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    for i in range(len(ciphertext_int)):
        if encrypt:
            value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        else:
            value = (ciphertext_int[i] + key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

plaintext = "HELLOWORLD"
key = "SECRET"
ciphertext = vigenere_cipher(plaintext, key)
print(f'The encrypted message is: {ciphertext}')

plaintext = vigenere_cipher(ciphertext, key, encrypt=False)
print(f'The decrypted message is: {plaintext}')
