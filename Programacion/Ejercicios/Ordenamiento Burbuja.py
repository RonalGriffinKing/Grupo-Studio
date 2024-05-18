my_list = [8, 10, 6, 2, 4]  # lista a ordenar
Largo=len(my_list)
cambio=True
while cambio:
    cambio=False
    for i in range(Largo-1):
        if my_list[i]>my_list[i+1]:
            cambio=True
            my_list[i], my_list[i+1]=my_list[i+1],my_list[i]
    
    



print(my_list)

