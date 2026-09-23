def count_words(s):
    s =s.lower()
    total = 0
    for mots in ["cat", "garden", "mice"]:
        total +=s.count(mots)
        total +=s.count(mots[::-1])
    return total

print(count_words("the CataCat attaCk a Cat"))
print(count_words("thE Cat's tactic wAS tO surpRISE thE mIce iN tHE gArdeN"))