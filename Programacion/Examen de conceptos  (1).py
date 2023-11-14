####Ejericio 1 
#print("****Calculo de la media de dos numeros****")
#numero1=int(input("Ingresa un numero:"))
#numero2=int(input("Ingresa el segundo numero:"))
#medida=(numero1+numero2)/2
#print(f"La media aritmetica de {numero1} y {numero2} es: {medida}")


####Ejericio 2
#print("****Caculadora de masa corporal IMC****")
#peso=float(input("Cuanto Pesa? "))
#altura=float(input("Cuanto mide? "))
#imc=round(peso/altura**2)
#print(f"Su IMC es {imc}")
#print("Un IMC muy alto indica obesidad.")

#####Ejericio 3

#print("****Convertidor de segundo a minutos:****")
#segundo=int(input("Ingresa la cantidad de segundo: Ejemplo: 1234: "))

#minutos=(segundo//60)
#segundos=segundo-minutos*60
#print(f"{segundo} segundos es igual a {minutos} Minutos con {segundos} Segundos")


#####Ejericio 4 Y 5

#print("****Divisor de numeros****")

#numero1=int(input("Ingresa el dividendo primero: "))
#numero2=int(input("Ingresa el dividendo segundo: "))

#if numero1==0:
#    print("No puedes dividir por 0")
#elif numero2==0:
#    print("No puedes divir por 0")
#else:
#    if numero1%numero2==0:
#        division=numero1/numero2
#        print(f"La division es exacta:{division}")
#    else:
#        division=numero1/numero23
#        resto=numero1%numero2
#        print(f"La division no es exacta. Cociente {division} Resto:{resto}")
 
####Ejerico 6

#print("Comparador de numeros")
#numero1=int(input("Ingresa el primer numero:"))
#numero2=int(input("Ingresa el segundo numero:"))

#if numero1>numero2:
#    print(f"El numero:{numero1} es mayor que {numero2}")
#elif numero1<numero2:
#    print(f"El numero {numero1} es menor que {numero2}")
#else:
#    print("Nada paso por aqui")



####Ejericio 7
#print("Comparador de años")
#year_actual=int(input("En que año estamos?:"))
#year_random=int(input("Escribe un año al azar:"))

#if year_actual==year_random:
#    print("Son el mismo año.")
#else:

#   if year_actual<year_random:
#        cuanto_mayor=year_random-year_actual
#        print(f"Para llegar al año {year_random} faltan {cuanto_mayor}")

#    else:
#        cuanto_mayor=year_actual-year_random
#        print(f"Desde el año {year_random} han pasado {cuanto_mayor} años.")

#####Ejericio 8
#print("Diga Sí para continuar")
#palabra=input("Desea continuar con el programa?")

#while palabra!="sì":
#    if palabra=="NO":
#        print("Hasta la vista.")
#        break
#    else:
#        palabra=input("Desea continuar con el programa?")
    
######Ejericio 9
#print("Confirme su contraseña:")
#contra=input("Ingrese su contraseña: ")
#confirmacion=input("Confirme su contraseña: ")


#while True:

#    if contra==confirmacion:
#        print("Contraseña confirmada")
#        break
#    else:
#        print("Las contraseñas no coinciden.")
#        contra=input("Ingrese su contraseña: ")
#       confirmacion=input("Confirme su contraseña: ")

#####Ejericio numero 10
#print("HUCHA")
#meta=int(input("Cuanto dinero quieres ahorrar?:"))
#ahorrado=0
#while True:
#    ahorros=int(input("Cuantos euros quieres meter?:"))
#    ahorrado=ahorrado+ahorros
#    if meta==ahorrado:
#        print(f"Objetivo conseguido ha ahorrado usted {ahorrado}")
#        break
#    elif meta<=ahorrado:
#        print(f"Objetivo conseguido ha ahorrado usted {ahorrado}")
#        break
#    else:
#        continue
    
 
 
######## Ejericio Extra
#####Ejericio numero 10
#print("HUCHA")
#meta=int(input("Cuanto dinero quieres ahorrar?:"))
#ahorrado=0
#while True:
    
#    if meta<=0:
#        print("La meta no puede ser 0")
#        meta=int(input("Cuanto dinero quieres ahorrar?:"))
#        meta=meta
#    else:
#        ahorros=int(input("Cuantos euros quieres meter?:"))
#        if ahorros<0:
#            print("No puedes ingresar negativos")
#            continue
#        else:
#            ahorrado=ahorrado+ahorros
#            if meta==ahorrado:
#                print(f"Objetivo conseguido ha ahorrado usted {ahorrado}")
#                break
#            elif meta<=ahorrado:
#                print(f"Objetivo conseguido ha ahorrado usted {ahorrado}")
#                break
#            else:
#                continue











