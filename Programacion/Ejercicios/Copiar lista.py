#Me puede copiar toda la lista

List_1=[4,5,62,3,5]
List_2=List_1[:]
List_1[0]=2
print(List_2)


#O puede copiar la hubaciones que yo necesito
List_1=[4,5,62,3,5]
List_2=List_1[1:4]
List_1[0]=2
print(List_2)