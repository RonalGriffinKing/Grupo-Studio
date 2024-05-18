def fibunacci(numero):
    if numero==0:
        return 1
    elif numero==1:
        return 1
    else:
        return fibunacci(numero - 2) + fibunacci(numero - 1)
while True:
    try:
        numero=int(input("Ingresa un numero:"))
        if numero<0:
            print("No numero negativos")
        else:
            print(f"El valor en la posicion {numero} es:",fibunacci(numero))
            break
    except ValueError:
        print("Ingresa un numero entero")
