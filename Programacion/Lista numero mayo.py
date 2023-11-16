lista=[17,3,11,5,1,9,7,15,13]
condicion=True
numero_mayor=0
numero_menor=lista[0]
suma=0
prom=0
largo=len(lista)

while condicion==True:
    for i in lista:
        suma+=i
        if i>numero_mayor:
            numero_mayor=i
        else:
            continue
    for i in lista:
        if i<=numero_menor:
            numero_menor=i
        
    condicion=False
prom=suma/largo
print(numero_mayor)
print(numero_menor)
print(prom)