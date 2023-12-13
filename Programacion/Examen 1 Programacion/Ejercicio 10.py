a=input("Ingresa el primer nombre: ").upper()
b=input("Ingresa el segundo nombre: ").upper()
lista1=a
lista2=b
largo=len(a)
largo2=len(b)
if a[0]==b[0]:
    print("True")
elif a[largo-1]==b[largo2-1]:
    print(True)
else:
    print("False")