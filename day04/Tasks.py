####### Task 1.2
import string


print("------- Task 1.2 ------")
number = int(input("Enter a number: "))
if number ==42:
    print("This is correct!")

####### Task 1.3
print("------- Task 1.3 ------")
number = int(input("Enter a number: "))
if number%2 == 0:
    print("This integer is even")
else:
    print("This integer is odd")

######## Task 1.4
print("------- Task 1.4 ------")
password = input("Enter a password: ")
if password == "open sesame":
    print("Access granted")
elif password == "will you open, you goddamn !@&/°":
    print("access fucking granted")
else:
    print("Access denied")

####### Task 1.5
print("------- Task 1.5 ------")
number= int(input("Enter a number: "))
result=""
if number == 42:
    result+="a"
if number <= 21:
    result+="b"
if number%2 ==0:
    result+="c"
if number%2 ==0 and (number <21):
    result+="d"
if number %2 !=0 and (number>=45):
    result+="e"

if result == "":                 
       result = "f"

print(result)

###### Task 1.6
print("------- Task 1.6 ------")
a = 42
b = 41
if a == b:
    print("A and B are the same")
if b <= a:
    print("B is equal to  or lower as A")
if b != a:
    print("B is different from A")

###### Task 2.1
print("------- Task 2.1 ------")
for i in range(1001):
    print(i)

###### Task 2.2
print("------- Task 2.2 ------")
phrase = input("Enter a phrase: ")
output = ""
for i in range(len(phrase)):
    output += phrase[i]
    output += phrase[i]
print(output)

###### Task 2.3
print("------- Task 2.3 ------")
for i in range(10000,0,-1):
    if i%7 == 0:
        print(i)

###### Task 2.4
print("------- Task 2.4 ------")
for i in range(-30,30,1):
    if i%3 == 0:
        print("Fizz") 
    if i%5 == 0:
        print("Buzz")
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    else:
        print(i)

###### Challenge 
print("------- Challenge ------")
while (val := input("Enter a digit: ")) and (s := input("Enter a string: ")):
    x = int(val)
    print(x if x >= 42 or any(c in "aeiouAEIOU" for c in s) else s)

###### Task 3.1
print("------- Task 3.1 -------")

def caesar_cipher(text,key):
    result=""
    for c in text:
        if c.isalpha():
            base =97 if c.islower() else 65
            result += chr((ord(c) - base + key) % 26 + base)
        else:
            result += c
    return result

text = input("Clear message: ")
key = int(input("Key between (1-25): "))
print(caesar_cipher(text, key))

##### Task 3.2
print("----- Task 3.2 ------")

cipher = input("Enter the ciphered text: ")

for key in range(26):
    print(key, caesar_cipher(cipher, -key))

###### Task 3.3 #######
def vigenere(text, key, decrypt=False):
    result = ""
    key = key.lower()
    shifts = [ord(c) - ord('a') for c in key]  ## Turn each key letter into a number => list of shifts 
    i = 0
    for ch in text: 
        if ch.isalpha():
            base = ord('a') if ch.islower() else ord('A')       
            shift = shifts[i % len(shifts)] ## wraps it around:
            if decrypt:
                shift = -shift
            result += chr((ord(ch) - base + shift) % 26 + base)
            i += 1
        else:
            result += ch

    return result

vigenere("hello world", "key", False)
vigenere("rijvs uyvjn", "key", True)


###### Task2.4 #####
print("------ Task 2.4 ------")
english_freq = {
    'a': 8.17, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70,
    'f': 2.23, 'g': 2.02, 'h': 6.09, 'i': 6.97, 'j': 0.15,
    'k': 0.77, 'l': 4.03, 'm': 2.41, 'n': 6.75, 'o': 7.51,
    'p': 1.93, 'q': 0.10, 'r': 5.99, 's': 6.33, 't': 9.06,
    'u': 2.76, 'v': 0.98, 'w': 2.36, 'x': 0.15, 'y': 1.97,
    'z': 0.07,
}


def score_text(text):
    counts = {}
    for ch in text:
        if ch.isalpha():
            ch = ch.lower()
            if ch in counts:
                counts[ch] = counts[ch] + 1
            else:
                counts[ch] = 1

    total = 0
    for ch in counts:
        total = total + counts[ch]

    if total == 0:
        return 999999

    score = 0
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for ch in alphabet:
        expected = english_freq[ch] / 100 * total
        if ch in counts:
            observed = counts[ch]
        else:
            observed = 0
        if expected > 0:
            score = score + (observed - expected) ** 2 / expected

    return score


def split_into_piles(ciphertext, key_length):
    letters = [ch.lower() for ch in ciphertext if ch.isalpha()]
    piles = [""] for _ in range(key_length)]
    for i, letter in enumerate(letters):
        piles[i % key_length] += letter
    return piles


# Crack one pile as a Caesar cipher
def crack_pile(pile):
    best_shift = 0
    best_score = 999999
    for shift in range(26):
        key_letter = chr(shift + ord('a'))
        candidate = vigenere(pile, key_letter, decrypt=True)
        score = score_text(candidate)
        if score < best_score:
            best_score = score
            best_shift = shift
    return best_shift


def recover_key(ciphertext, key_length):
    return "".join(chr(crack_pile(pile) + ord('a'))
                   for pile in split_into_piles(ciphertext, key_length))


ciphertext = input("Ciphered text: ")
key_length = int(input("Key length: "))
key = recover_key(ciphertext, key_length)
print("Recovered key:", key)
print("Plaintext    :", vigenere(ciphertext, key, decrypt=True))