
nombres = []
contador=0
while True:
    nombre = input("Ingrese un nombre (o escriba -1 para terminar): ").upper()

    if nombre == "-1":
        break

    nombres.append(nombre)

nombres_contador = []

for nombre in nombres:
    if nombre in nombres_contador:
        continue
    nombres_contador.append(nombre)
    contador = 0
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            contador += 1
    print(f"El nombre {nombre} se repite {contador} veces.")