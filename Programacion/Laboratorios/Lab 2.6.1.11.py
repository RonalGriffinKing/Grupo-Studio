hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))


#% RESTOS
minutos=(mins+dura)%60
horas=(hour+(mins+dura)//60)%24


print("Horas",horas)
##print(modulo)
print(minutos)
# Write your code here.

print("Termina",horas,":",minutos)