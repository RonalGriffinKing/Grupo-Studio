my_list=[17,3,5,7,9,32,2,7,5,6]

largest=my_list[0]
menor=my_list[0]
for i in range(1,len(my_list)):
    if my_list[i]>largest:
        largest=my_list[i]

print(largest)