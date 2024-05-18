list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
print("Tu lista es:",list)
print("Que operacion quieres hacer?")
print("*1 Sumar \n*2 Multiplicar \n*3 Dividir \n*-1 Salir")
opcion=int(input())

largo=len(list)
while opcion!="":
    if opcion==1:
        valor=int(input("Ingresa el valor para sumar:"))
        for x in range(largo):
            list[x]=list[x]+valor
        print(list)
        print("Que operacion quieres hacer?")
        print("*1 Sumar \n*2 Multiplicar \n*3 Dividir \n*-1 Salir")
        opcion=int(input())
        if opcion==-1:
            break
        else:
            continue
    elif opcion==2:
        valor=int(input("Ingresa el valor para multiplicar:"))
        for x in range(largo):
            list[x]=list[x]*valor
        print(list)
        print("Que operacion quieres hacer?")
        print("*1 Sumar \n*2 Multiplicar \n*3 Dividir \n*-1 Salir")
        opcion=int(input())
        if opcion==-1:
            break
        else:
            continue
    elif opcion==3:
        valor=int(input("Ingresa el valor para dividir:"))
        for x in range(largo):
            list[x]=list[x]//valor
        print(list)
        print("Que operacion quieres hacer?")
        print("*1 Sumar \n*2 Multiplicar \n*3 Dividir \n*-1 Salir")
        opcion=int(input())
        if opcion==-1:
            break
        else:
            continue

    elif opcion==4:
        print("Quieres Eliminar la lista?")
        print("*1 Si \n*2 No")
        opcion=int(input())
        if opcion==1:
            for z in range(largo):
                print(list[0])
                del list[0]
    
        else:
            continue
    break
