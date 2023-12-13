a=input("Ingrese un texto: ").upper()
print("El caracter inicial es",a[0])

largo=len(a)
print("Ingresa un numero menor que:",largo,"", end=":")
b=int(input())

print("El caracter en esa posicion es",a[b-1])

