palabras="Hola(como)estas"

for i in range(len(palabras)):
    if palabras[i]=="(":
        parentesis1=i
    elif palabras[i]==")":
        parentesis2=i

palabra1=palabras[:parentesis1]
palabra_central=(palabras[parentesis1+1:parentesis2])[::-1]
palabra_final=palabras[parentesis2+1:]
print(palabra1)
print(palabra_central)
print(palabra_final)
print(palabra_final+"("+palabra_central+")"+palabra1)


