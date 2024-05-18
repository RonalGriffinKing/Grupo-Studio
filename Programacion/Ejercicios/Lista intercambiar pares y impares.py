my_list=[1,2,3,4,5,6,7,8,9,10,31,45,60,70]
largo=len(my_list)
lista_pares=[]
lista_impares=[]
for i in range(largo):
    if my_list[i]%2==0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

for i in range(len(my_list)//2):
    my_list[lista_pares[i]],my_list[lista_impares[i]]=my_list[lista_impares[i]],my_list[lista_pares[i]]

print(my_list)
