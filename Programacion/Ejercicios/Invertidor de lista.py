variable=int(input("Ingresa un numero o termina -1:"))
lista=[]

while variable!=-1:
    lista.append(variable)
    variable=int(input("Ingresa un numero o termina -1:"))
print(lista)
largo=len(lista)

for i in range(largo):
    lista.insert(lista[largo-1],lista[i])
print(lista)
    
largo=len(lista)
for i in range(largo//2):
    del lista[0]
print(lista)    
