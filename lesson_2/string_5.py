text = input("insert your word: ")

vowels = ""
consonants = ""

for char in text.lower():
    if char in "aeiou":  
        vowels += char
    elif char.isalpha():
        consonants += char
vowels_cn = len(vowels)
consonants_cn = len(consonants)
print("Vowels:", vowels_cn)
print("Consonants:", consonants_cn)
