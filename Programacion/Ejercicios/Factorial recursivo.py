def factorial(numero):
    if numero==0:
        return 1
    else:
        return numero * factorial(numero-1)

while True:
    try:
        numero=int(input("Ingresa un numero:"))
        if numero<0:
            print("No numero negativos")
        else:
            print("El factorial es:",factorial(numero))
            break
    except ValueError:
        print("Ingresa un numero entero.")

