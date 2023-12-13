a=input("Ingresa una frase:")

contador_vocales=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
        contador_vocales=contador_vocales+1
print(contador_vocales)