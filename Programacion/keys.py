import faker as f

diccionario = {}

for i in range(10):
    diccionario[i] = f.Faker().name()

diccionario[10] = "Ronal"
#Puedo crear una una llave con un valor directamente creandolo asi, tambien si la llave ya existe le cambiara el valor 
diccionario[11]=1
diccionario[11]+=2
for i in range(12):
    print(diccionario[i])

#Eliminar una clave
del diccionario[11]
for i in range(11):
    print(diccionario[i])

#Recorrer diccionario
for i in diccionario:
    print("Recoriendo diccionario")
    print(diccionario[i])

#Eliminar el ultimo item
diccionario.popitem()
for i in diccionario:  
    print(diccionario[i])
