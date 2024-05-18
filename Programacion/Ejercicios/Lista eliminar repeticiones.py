my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_lista_unica=[]

for i in my_list:
    if i not in my_lista_unica:
        my_lista_unica.append(i)

print("La lista con elementos repetidos:")
print(my_lista_unica)
