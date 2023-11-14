hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("Esta es tu lista",hat_list)
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero=int(input("Ingrese un numero para remplazar:"))
hat_list[2]=numero
print("Lista con el numero nuevo:")
print(hat_list)

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.

del hat_list[4]
print("Lista con el numero eliminado:")
print(hat_list)

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("Larga de la lista:")
print(len(hat_list))

