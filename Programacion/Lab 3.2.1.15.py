c0=int(input("Ingrese un numero: "))
contador=0
while c0>0:
    if c0%2==0:
        c0=c0/2
        
    else:
        c0=3*c0+1
    contador+=1
    print(int(c0))
    if c0!=1:
        continue
    else:
        break
print("Pasos:",contador)

