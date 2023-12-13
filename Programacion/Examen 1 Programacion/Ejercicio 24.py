
cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")
cadena_intercambiada = cadena2[:2] + cadena1[2:] + " " + cadena1[:2] + cadena2[2:]

print(f"Cadenas con caracteres intercambiados: {cadena_intercambiada}")
