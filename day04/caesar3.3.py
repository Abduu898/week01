"""
Task 3.3 — Encrypt and decrypt with the Vigenère cipher.
The user enters the text and the key.
"""

def vigenere(text, key, decrypt=False):
    """Vigenère cipher. Set decrypt=True to reverse the shifts."""
    result = ""
    key = key.lower()
    shifts = [ord(c) - ord('a') for c in key]
    i = 0

    for ch in text:
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')
            shift = shifts[i % len(shifts)]
            if decrypt:
                shift = -shift
            result += chr((ord(ch) - base + shift) % 26 + base)
            i += 1
        else:
            result += ch

    return result


mode = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()
text = input("Enter the text: ")
key  = input("Enter the key: ")

if mode == 'e':
    print("Encrypted:", vigenere(text, key, decrypt=False))
elif mode == 'd':
    print("Decrypted:", vigenere(text, key, decrypt=True))
else:
    print("Invalid mode. Type 'e' or 'd'.")
