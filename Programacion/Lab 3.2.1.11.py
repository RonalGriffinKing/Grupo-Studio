word_without_vowels = ""


print("Ingresa una PALABRA:")
user_word=(input())
user_word=user_word.upper()
palabra=""

for letter in user_word:
    if letter=="A":
        continue    
    elif  letter=="E":
        continue
    elif  letter=="I":
        continue
    elif letter=="O":
        continue
    elif letter=="U":
        continue
    else:
        palabra=palabra+letter
print(palabra)
# Imprimir la palabra asignada a word_without_vowels.
