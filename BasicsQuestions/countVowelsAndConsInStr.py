text = "education"
vowel = 0
consonent = 0

for i in text :

    if i in "aeiou":
        vowel += 1

    else:
        consonent += 1

print(vowel)
print(consonent)