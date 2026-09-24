import string

ENGLISH_FREQ = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
    'z': 0.07,
}


def vigenere(text, key, decrypt=False):
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


def score_text(text):
    """Chi-squared score vs English. Lower = more English-like."""

    counts = {}

    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            counts[ch] = counts.get(ch, 0) + 1

    total = sum(counts.values())

    if total == 0:
        return 999999

    score = 0

    for ch in string.ascii_lowercase:
        expected = ENGLISH_FREQ[ch] / 100 * total
        observed = counts.get(ch, 0)

        if expected > 0:
            score += (observed - expected) ** 2 / expected

    return score


def split_into_piles(ciphertext, key_length):
    """Split letters into key_length piles (one per key position)."""

    letters = [ch.lower() for ch in ciphertext if ch.isalpha()]

    piles = [""] * key_length

    for i, letter in enumerate(letters):
        piles[i % key_length] += letter

    return piles


def crack_pile(pile):
    """Try all 26 Caesar shifts on one pile; return the best shift."""

    best_shift = 0
    best_score = 999999

    for shift in range(26):

        key_letter = chr(shift + ord('a'))

        candidate = vigenere(
            pile,
            key_letter,
            decrypt=True
        )

        s = score_text(candidate)

        if s < best_score:
            best_score = s
            best_shift = shift

    return best_shift


def recover_key(ciphertext, key_length):
    """Recover the Vigenère key by cracking each pile as Caesar."""

    piles = split_into_piles(ciphertext, key_length)

    key = ""

    for pile in piles:
        shift = crack_pile(pile)
        key += chr(shift + ord('a'))

    return key


# --- Main ---

ciphertext = input("Ciphered text: ")

key_length = int(input("Key length: "))

key = recover_key(ciphertext, key_length)

print("Recovered key:", key)

print(
    "Plaintext    :",
    vigenere(ciphertext, key, decrypt=True)
)
