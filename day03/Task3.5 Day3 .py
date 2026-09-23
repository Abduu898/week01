###### Task 3.5
print("-------");
text= input("Enter a text: ").lower()
frequency= {}
for i in text:
    if i in frequency and i.isalpha():
        frequency[i]+=1
    elif i.isalpha():
        frequency[i]=1

total= sum(frequency.values())
print ("tota of each letter in the text: ",total)
percentage= {}
for l in frequency:
    percentage[l]= (frequency[l]/total)
    percentage[l]= percentage[l]*100
    percentage[l]= round(percentage[l], 6)
    

print("percentage of each letter in the text: ",percentage)


languages = {
    "English": {'a': 8.16, 'b': 1.49, 'c': 2.78, 'd': 4.25, 'e': 12.70, 'f': 2.22, 'g': 2.01, 'h': 6.09, 'i': 6.96, 'j': 0.15, 'k': 0.77, 'l': 4.02, 'm': 2.40, 'n': 6.74, 'o': 7.50, 'p': 1.92, 'q': 0.09, 'r': 5.98, 's': 6.32, 't': 9.05, 'u': 2.75, 'v': 0.97, 'w': 2.36, 'x': 0.15, 'y': 1.97, 'z': 0.07},
    "French":  {'a': 7.63, 'b': 0.90, 'c': 3.26, 'd': 3.66, 'e': 14.71, 'f': 1.06, 'g': 0.86, 'h': 0.73, 'i': 7.52, 'j': 0.61, 'k': 0.04, 'l': 5.45, 'm': 2.96, 'n': 7.09, 'o': 5.39, 'p': 3.02, 'q': 1.36, 'r': 6.55, 's': 7.94, 't': 7.24, 'u': 6.31, 'v': 1.62, 'w': 0.11, 'x': 0.38, 'y': 0.30, 'z': 0.13, 'é': 1.90, 'è': 0.27, 'à': 0.48, 'ç': 0.08, 'ê': 0.22},
    "German":  {'a': 6.51, 'b': 1.89, 'c': 3.06, 'd': 5.08, 'e': 17.40, 'f': 1.66, 'g': 3.01, 'h': 4.76, 'i': 7.55, 'j': 0.27, 'k': 1.21, 'l': 3.44, 'm': 2.53, 'n': 9.78, 'o': 2.51, 'p': 0.79, 'q': 0.02, 'r': 7.00, 's': 7.27, 't': 6.15, 'u': 4.35, 'v': 0.67, 'w': 1.89, 'x': 0.03, 'y': 0.04, 'z': 1.13, 'ä': 0.57, 'ö': 0.44, 'ü': 0.99, 'ß': 0.30},
    "Spanish": {'a': 11.52, 'b': 2.21, 'c': 4.01, 'd': 5.01, 'e': 12.18, 'f': 0.69, 'g': 1.76, 'h': 0.70, 'i': 6.24, 'j': 0.49, 'k': 0.01, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'o': 8.68, 'p': 2.51, 'q': 0.87, 'r': 6.87, 's': 7.97, 't': 4.63, 'u': 3.10, 'v': 0.90, 'w': 0.01, 'x': 0.22, 'y': 0.89, 'z': 0.52, 'ñ': 0.31, 'á': 0.50, 'é': 0.43, 'í': 0.72, 'ó': 0.82, 'ú': 0.16},
    "Italian": {'a': 11.74, 'b': 0.92, 'c': 4.50, 'd': 3.73, 'e': 11.79, 'f': 0.95, 'g': 1.64, 'h': 1.54, 'i': 11.28, 'j': 0.01, 'k': 0.01, 'l': 6.51, 'm': 2.51, 'n': 6.88, 'o': 9.83, 'p': 3.05, 'q': 0.51, 'r': 6.37, 's': 4.98, 't': 5.62, 'u': 3.01, 'v': 2.10, 'w': 0.01, 'x': 0.01, 'y': 0.01, 'z': 0.49, 'à': 0.63, 'è': 0.26, 'é': 0.15, 'ì': 0.03, 'ò': 0.02, 'ù': 0.01}
}

scores = {}
for lang, ref in languages.items():
        diff = 0
        for letter, ref_pct in ref.items():
            diff += abs(percentage.get(letter, 0) - ref_pct)
        scores[lang] = diff

print("Scores:", scores)
best = min(scores, key=scores.get)
print("Detected language:", best)