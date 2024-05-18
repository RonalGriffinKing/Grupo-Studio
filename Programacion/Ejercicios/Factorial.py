#Factorial de un numero
def factorial():
    num=int(input("Ingresa un numero:"))    
    if num<0:  
        print("No Negativos")
    else:
        factorial=1
        for i in range(1,num+1):
            factorial*=i
        print(factorial)
try:
    factorial()
     
except ValueError:
    print("No es un numero:")
    factorial()

