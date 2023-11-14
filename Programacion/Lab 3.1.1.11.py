income = float(input("Introduce el ingreso anual:"))

#
# Escribe tu código aquí.
#
if  income>=1001 and income <= 85528 :
    tax=((income*18)/100)-556.02
elif income >= 85528:
    excedente=((income-85528)/100)*32
    tax=14839.02+excedente
else:
    tax=0.0

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")

