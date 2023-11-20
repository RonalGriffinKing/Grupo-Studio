lista=[17,3,11,5,1,9,7,15,13]
condicion=True
to_find=int(input("Ingresa el numero que quieres buscar:"))
largo=len(lista)
indice=0
while condicion==True:
    for i in range(largo):
        if lista[i]==to_find:
            print(i)
            indice=i
            condicion=False
print("EL numero se encuentra en el indice",indice)