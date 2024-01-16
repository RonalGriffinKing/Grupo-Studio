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

imten1 = diccionario.get(1)
print("Extraciion con get de diccionario:",imten1)

#Update de un diccionario
diccionario.update({12:"Juan"})
print(diccionario[12])

#Otro diccionario revisar si esta en mi diccionario
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

if "zamek" in pol_esp_dictionary:
    print("Si")
else:
    print("No")


#Copiar diccionario
pol_esp_dictionary = {
    "zamek" : "castillo",
    "woda"  : "agua",
    "gleba" : "tierra"
    }

copy_dictionary = pol_esp_dictionary.copy()

#Diccionario con items en español
spanish_dictionary = {
    "zamek": "castillo",
    "woda": "agua",
    "gleba": "tierra"
}