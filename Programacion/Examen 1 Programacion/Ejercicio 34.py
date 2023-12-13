lista1=[2,5,1,8]
lista2=[3,1,6,7]
largo=len(lista2)
for i in range(0,len(lista1)):
    if lista1[i] > lista2[largo-1]:
        print("True")
    else:
        print("False")