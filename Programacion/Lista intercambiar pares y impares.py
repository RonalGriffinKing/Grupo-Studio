my_list=[1,2,3,4,5,6,7,8,9,10,1,2,3,4]
largo=len(my_list)
lista_pares=[]
lista_impares=[]
print(my_list)
for i in range(0,largo):
    if my_list[i]%2==0:
        lista_pares.append(my_list[i])
    else:
        lista_impares.append(my_list[i])
for i in range(largo//2):
    my_list[lista_pares[i]],my_list[lista_impares[i]]=my_list[lista_impares[i]],my_list[lista_pares[i]]
print(my_list)
print("la lista de pares es:",lista_pares)
print("la lista de impares es:",lista_impares)