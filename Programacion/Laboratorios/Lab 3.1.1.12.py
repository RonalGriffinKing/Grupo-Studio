year = int(input("Introduce un año:"))

if year <1582:
    print("No esto dentro del periodo del calendario")

elif year%4==0:
    print("Es un año comun")
elif year%10 != 0:
    print("Es un año bisiesto")
    
else:
    print("No entiendo el año")
#
# Escribe tu código aquí.

