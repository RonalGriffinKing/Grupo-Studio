import random
EMPTY = "-"
PAWN = "♟"
ROOK = "♜"
KNIGHT = "♞"
QUEEN="♚"
KING="♛"
ALFIL="♝"

BPAWN = "♙"
BROOK = "♖"
BKNIGHT = "♘"
BQUEEN="♔"
BKING="♕"
BALFIL="♗"

board = []
row2 = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

print("     0   1    2    3    4    5    6    7")

board[0][0] = ROOK
board[0][7] = ROOK
board[7][0] = BROOK
board[7][7] = BROOK

board[0][1] = KNIGHT
board[0][6] = KNIGHT
board[7][1] = BKNIGHT
board[7][6] = BKNIGHT

board[0][2] = ALFIL
board[0][5] = ALFIL
board[7][2] = BALFIL
board[7][5] = BALFIL

board[0][3] = KING
board[0][4] = QUEEN
board[7][3] = BKING
board[7][4] = BQUEEN

for i in range(8):
    board[1][i]=PAWN
    board[6][i]=BPAWN

for i in range(8):

    print(i,board[i])
    



def jugadornegro():
    m=input("Que quieres mover: Ingresa [P, T, C, Q, K, A]:").upper()
    if m=="P":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        if Posicion_X==1:
            print("Puedes avanzar 2")
            Posicion_X2=int(input("Ingresa la posicion nueva peon X:"))
            Posicion_Y2=int(input("Ingresa la posicion nueva peon y:"))
                

        
           
    elif m=="T":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva de la torre X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva de la torre y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    
    elif m=="C":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva del caballo X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva del caballo y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    elif m=="Q":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva de la reina X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva de la reina y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    elif m=="K":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva de la REY X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva de la REY y:"))
        board[Posicion_Y2][Posicion_X2]=Monito

    elif m=="A":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva del alfil X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva del alfil y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    for i in range(8):
        print(i,board[8]) 



def jugadorblanco():
    m=input("Que quieres mover: Ingresa [P, T, C, Q, K, A]:").upper()
    if m=="P":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva peon X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva peon y:"))
    elif m=="T":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva de la torre X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva de la torre y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    
    elif m=="C":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva del caballo X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva del caballo y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    elif m=="Q":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva de la reina X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva de la reina y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    elif m=="K":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva de la REY X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva de la REY y:"))
        board[Posicion_Y2][Posicion_X2]=Monito

    elif m=="A":
        Posicion_X=int(input("Ingresa la posicion x:"))
        Posicion_Y=int(input("Ingresa la posicion y:"))
        Monito=board[Posicion_Y][Posicion_X]
        board[Posicion_Y][Posicion_X]=EMPTY
        Posicion_X2=int(input("Ingresa la posicion nueva del alfil X:"))
        Posicion_Y2=int(input("Ingresa la posicion nueva del alfil y:"))
        board[Posicion_Y2][Posicion_X2]=Monito
    for i in range(8):
        print(i,board[8]) 
nombre=input("Ingresa el nombre del jugador:").upper()
nombre2=input("Ingresa el nombre del segundo jugador:").upper()
ramdon=random.randint(0,1)
if ramdon==0:
    print("El primer jugador es:",nombre,"Jugador Blanco")
    print("El segundo jugador es:",nombre2,"Jugador Negro")
    print("***Empieza el juego***")
    print("Tu inicio es:",nombre,"Jugador Blanco")
    jugadornegro()
else:
    print("El primer jugador es:",nombre2,"Jugador Negro")
    print("El segundo jugador es:",nombre,"Jugador Blanco")
    print("***Empieza el juego***")
    print("Tu inicio es:",nombre2,"Jugador Negro")
    jugadornegro()