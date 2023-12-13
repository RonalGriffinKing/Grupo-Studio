a=int(input("Ingresa un numero para ver divisores positivos: "))
for i in range(1,a+1):
    if a%i==0:
        print(i)
