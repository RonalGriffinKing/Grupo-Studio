
nombres = []
contador=0
while True:
    nombre = input("Ingrese un nombre (o escriba -1 para terminar): ").upper()

    if nombre == "-1":
        break

    nombres.append(nombre)

nombres_no_duplicados = []

for nombre in nombres:
    if nombre in nombres_no_duplicados:
        continue
    nombres_no_duplicados.append(nombre)
    contador = 0
    for i in range(len(nombres)):
        if nombres[i] == nombre:
            contador += 1
print(nombres_no_duplicados)
