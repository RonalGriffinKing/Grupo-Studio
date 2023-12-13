a=input("Ingrese un frase:")

for i in a:
    if i==" ":
        del i
    elif i=="":
        del i
cantidad=len(a)


if cantidad%2==0:
    print(False)
else:
    print(True)
