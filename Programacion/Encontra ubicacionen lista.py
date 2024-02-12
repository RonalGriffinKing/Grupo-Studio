#Recursividad

import faker as f
diccionario = {}
def generador():
    for i in range(10):
        diccionario[i] = f.Faker().name()

    diccionario[10] = "Ronal"
    return diccionario

print(generador())
