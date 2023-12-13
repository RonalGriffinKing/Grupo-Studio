a=int(input("Ingresa el primer numero:"))
b=int(input("Ingresa el segundo numero:"))
c=int(input("Ingresa el tercer numero:"))
numero_menor=a
if b<numero_menor:
    numero_menor=b
if c<numero_menor:
    numero_menor=c
print("El numero menor es:",numero_menor)