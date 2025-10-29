
def make_board(string):
    brett = [["_" for i in range(8)] for j in range(8)]
    teller = 0
    for i in range(8):
        for j in range(8):
            if string[teller] == ".":
                brett[i][j] = "_"
            else:
                brett[i][j] = string[teller]
            teller += 1

    return brett

def get_piece(board, x, y):
    x, y = y, x
    x = -x + 8
    y = y - 1 
    return board[x][y], x, y



def get_legal_moves(board,x,y):
    liste = []

    # må lage til, tårn, springer, hest, dronning, konge. Både hvit og svart til hver.
    #bonde
    if get_piece(board,x,y)[0] == "♙":
        #finner ut om den kan gå fremmover
        if get_piece(board,x,y-1)[0] == "_":
            if y == 7:
                if get_piece(board,x,y-2)[0] == "_":
                    liste.append((x,y-2))
            liste.append((x,y-1))    
        #finner ut om den kan gå på skrå
        if get_piece(board,x-1,y-1)[0] != "_" and ord(get_piece(board,x-1,y-1))[0] < 91:
            liste.append((x-1,y-1))
        if get_piece(board,x+1,y-1)[0] != "_" and ord(get_piece(board,x+1,y-1))[0] < 91:
            liste.append((x+1,y-1))
        
            
    elif get_piece(board,x,y)[0] == "♟":
        #finner ut om den kan gå fremover
        if get_piece(board,x,y+1)[0] == "_":
            if y == 2:
                if get_piece(board,x,y+2)[0] == "_":
                    liste.append((x,y+2))
            liste.append((x,y+1))
        #finner ut om den kan gå på skrå
        if get_piece(board,x-1,y+1)[0] != "_" and ord(get_piece(board,x-1,y+1))[0] > 96:
            liste.append((x-1,y+1))
        if get_piece(board,x+1,y+1)[0] != "_" and ord(get_piece(board,x+1,y+1))[0] > 96:
            liste.append((x+1,y+1))

    return liste

def move_piece(board, x1, y1, x2, y2):
    if (x2,y2) in get_legal_moves(board,x1,y1):
        brikke, x, y = get_piece(board,x1,y1)
        board[x][y] = "_"
        nyx, nyy = get_piece(board,x2,y2)[1], get_piece(board,x2,y2)[2]
        board[nyx][nyy] = brikke
    else:
        print("Du må skrive gyldige koordinater")


def sjekk_sjakk(board):
    # lagre kongens posisjon, og alle posisjoner rundt kongen der en brikke må stå for å sette kongen i sjakk, hvis så returner true else false
    pass

def sjekk_sjakk_matt(board):
    # lagre kongens posisjon, sjekk om sjekk_sjakk = true, så se om get_legal_moves returnerer tom liste.
    pass

def visbrett(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(f"{board[i][j]}", end=" ")
        print("",end="\n")
    print()


board_string_1 = "♖♘♗♕♔♗♘♖♙♙♙♙♙♙♙♙................................♟♟♟♟♟♟♟♟♜♞♝♛♚♝♞♜"
#"♖, ♜, ♗, ♝, ♘, ♞, ♕, ♛, ♔, ♚, ♙, ♟"
board = make_board(board_string_1)


visbrett(board)
move_piece(board,2,7,2,5)
visbrett(board)


# en while løkke for kjøring, hvor du sjekker om man er i sjakkmatt, eller sjakk, spørre om hvor du vil 

#print(get_piece(board, 2,2))
# print(get_legal_moves(board,2,7))