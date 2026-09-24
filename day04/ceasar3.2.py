
def caesar_cipher(text, key):
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c
    return result


cipher = input("Enter the ciphered text: ")
for key in range(26):
    print(key, caesar_cipher(cipher, -key))
