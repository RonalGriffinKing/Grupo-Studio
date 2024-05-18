# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

Palabra=input("Ingresa la palabra secreta:").upper()
Largo=len(Palabra)
Intentos=6
Letras=[]
Formando=[]
for i in Palabra :
    Letras.append(i)
    Formando.append("[ ]")
while Intentos!=0:
    print(AHORCADO[Intentos])
    print(Formando)
    Letra=input("Ingresa una Letra:").upper()
    for i in range(Largo):
        acertaste=False
        if Letras[i]==Letra:
            print("Salvado")
            Formando[i]=Letra
            acertaste=True
    if acertaste==False:
        Intentos=Intentos-1
print("Perdiste")
print(AHORCADO[0])