#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4)
#y diga cuántos días tiene (por ejemplo, 30) y el nombre del mes.
#Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días
Lista=["Enero :31 Dias","Febrero: 28 Dias","Marzo: 31 Dias"]

mes=int(input("Ingresa el  numero del mes que quieres conocer:"))
Condicion=True
mes=mes-1
Largo=len(Lista)
while Condicion:
    for i in range(Largo):
        if i==mes:
            Condicion=False
            print(Lista[i])
