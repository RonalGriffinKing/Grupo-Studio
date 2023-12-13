a=input("Ingresa un texto para buscar su posicion de la vocal y la vocal: ")

for i in range(len(a)):
    if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
        print("La vocal es:",a[i])
        print("Su posicion es:",i)