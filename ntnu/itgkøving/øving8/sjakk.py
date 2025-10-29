hvitebrikker = ["♜","♝","♞","♛","♚","♟"]
svartebrikker = ["♖","♗","♘","♕","♔","♙"]

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
    #"♕, ♛,"
    # må lage til dronning. Både hvit og svart til hver.
    # trengs å sjekke at man setter sin egen konge i sjakk
    #bonde
    if get_piece(board,x,y)[0] == "♙":
        #finner ut om den kan gå fremmover
        if get_piece(board,x,y-1)[0] == "_":
            if y == 7:
                if get_piece(board,x,y-2)[0] == "_":
                    liste.append((x,y-2))
            liste.append((x,y-1))    
        #finner ut om den kan gå på skrå
        if get_piece(board,x-1,y-1)[0] != "_" and get_piece(board,x-1,y-1)[0] in hvitebrikker:
            liste.append((x-1,y-1))
        if get_piece(board,x+1,y-1)[0] != "_" and get_piece(board,x+1,y-1)[0] in hvitebrikker:
            liste.append((x+1,y-1))
        
            
    elif get_piece(board,x,y)[0] == "♟":
        #finner ut om den kan gå fremover
        if get_piece(board,x,y+1)[0] == "_":
            if y == 2:
                if get_piece(board,x,y+2)[0] == "_":
                    liste.append((x,y+2))
            liste.append((x,y+1))
        #finner ut om den kan gå på skrå
        if get_piece(board,x-1,y+1)[0] != "_" and get_piece(board,x-1,y+1)[0] in svartebrikker:
            liste.append((x-1,y+1))
        if get_piece(board,x+1,y+1)[0] != "_" and get_piece(board,x+1,y+1)[0] in svartebrikker:
            liste.append((x+1,y+1))
   
    #tårn
    if get_piece(board,x,y)[0] == "♖":
        # til venstre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1)[0] == "_" and x1 > 1:
                liste.append((x1-1,y1))
                x1 -= 1
            if get_piece(board,x1-1,y1)[0] in hvitebrikker and x1 > 1:
                liste.append((x1-1,y1))
        except IndexError:
            pass
        # til høyre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1)[0] == "_":
                liste.append((x1+1,y1))
                x1 += 1
            if get_piece(board,x1+1,y1)[0] in hvitebrikker:
                liste.append((x1+1,y1))
        except IndexError:
            pass
        # oppver
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1-1)[0] == "_" and y1 > 1:
                liste.append((x1,y1-1))
                y1 -= 1
            if get_piece(board,x1,y1-1)[0] in hvitebrikker and y1 > 1:
                liste.append((x1,y1-1))
        except IndexError:
            pass
        # nedover
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1+1)[0] == "_" and y1 < len(board):
                liste.append((x1,y1+1))
                y1 += 1
            if get_piece(board,x1,y1+1)[0] in hvitebrikker and y1 < len(board):
                liste.append((x1,y1+1))
        except IndexError:
            pass

    elif get_piece(board,x,y)[0] == "♜":
        # til venstre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1)[0] == "_" and x1 > 1:
                liste.append((x1-1,y1))
                x1 -= 1
            if get_piece(board,x1-1,y1)[0] in svartebrikker and x1 > 1:
                liste.append((x1-1,y1))
        except IndexError:
            pass
        # til høyre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1)[0] == "_":
                liste.append((x1+1,y1))
                x1 += 1
            if get_piece(board,x1+1,y1)[0] in svartebrikker:
                liste.append((x1+1,y1))
        except IndexError:
            pass
        # oppver
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1-1)[0] == "_" and y1 > 1:
                liste.append((x1,y1-1))
                y1 -= 1
            if get_piece(board,x1,y1-1)[0] in svartebrikker and y1 > 1:
                liste.append((x1,y1-1))
        except IndexError:
            pass
        # nedover
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1+1)[0] == "_" and y1 < len(board):
                liste.append((x1,y1+1))
                y1 += 1
            if get_piece(board,x1,y1+1)[0] in svartebrikker and y1 < len(board):
                liste.append((x1,y1+1))
        except IndexError:
            pass
    #konge
    if get_piece(board,x,y)[0] == "♔":
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                try:
                    if get_piece(board,i,j)[0] == "_" or get_piece(board,i,j)[0] in hvitebrikker:
                        liste.append((i,j))
                except IndexError:
                    pass
    elif get_piece(board,x,y)[0] == "♚":
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                try:
                    if get_piece(board,i,j)[0] == "_" or get_piece(board,i,j)[0] in svartebrikker:
                        liste.append((i,j))
                except IndexError:
                    pass
    #springer
    if get_piece(board,x,y)[0] == "♗":
        #NØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1+1)[0] == "_" and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
                y1 += 1
                x1 += 1
            if get_piece(board,x1+1,y1+1)[0] in hvitebrikker and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
        except IndexError:
            pass
        #SØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1-1)[0] == "_" and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
                y1 -= 1
                x1 += 1
            if get_piece(board,x1+1,y1-1)[0] in hvitebrikker and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
        except IndexError:
            pass
        #SV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1-1)[0] == "_" and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
                y1 -= 1
                x1 -= 1
            if get_piece(board,x1-1,y1-1)[0] in hvitebrikker and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
        except IndexError:
            pass
        #NV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1+1)[0] == "_" and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
                y1 += 1
                x1 -= 1
            if get_piece(board,x1-1,y1+1)[0] in hvitebrikker and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
        except IndexError:
            pass
    elif get_piece(board,x,y)[0] == "♝":
        #NØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1+1)[0] == "_" and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
                y1 += 1
                x1 += 1
            if get_piece(board,x1+1,y1+1)[0] in svartebrikker and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
        except IndexError:
            pass
        #SØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1-1)[0] == "_" and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
                y1 -= 1
                x1 += 1
            if get_piece(board,x1+1,y1-1)[0] in svartebrikker and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
        except IndexError:
            pass
        #SV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1-1)[0] == "_" and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
                y1 -= 1
                x1 -= 1
            if get_piece(board,x1-1,y1-1)[0] in svartebrikker and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
        except IndexError:
            pass
        #NV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1+1)[0] == "_" and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
                y1 += 1
                x1 -= 1
            if get_piece(board,x1-1,y1+1)[0] in svartebrikker and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
        except IndexError:
            pass
    #hest
    if get_piece(board,x,y)[0] == "♘":
        try:
            x1, y1 = x, y
            if get_piece(board,x1+2,y1-1)[0] == "_" or get_piece(board,x1+2,y1-1)[0] in hvitebrikker:
                liste.append((x1+2,y1-1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1+2,y1+1)[0] == "_" or get_piece(board,x1+2,y1+1)[0] in hvitebrikker:
                liste.append((x1+2,y1+1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-2,y1-1)[0] == "_" or get_piece(board,x1-2,y1-1)[0] in hvitebrikker:
                liste.append((x1-2,y1-1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-2,y1+1)[0] == "_" or get_piece(board,x1-2,y1+1)[0] in hvitebrikker:
                liste.append((x1-2,y1+1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-1,y1+2)[0] == "_" or get_piece(board,x1-1,y1+2)[0] in hvitebrikker:
                liste.append((x1-1,y1+2))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1+1,y1+2)[0] == "_" or get_piece(board,x1+1,y1+2)[0] in hvitebrikker:
                liste.append((x1+1,y1+2))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-1,y1-2)[0] == "_" or get_piece(board,x1-1,y1-2)[0] in hvitebrikker:
                liste.append((x1-1,y1-2))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1+1,y1-2)[0] == "_" or get_piece(board,x1+1,y1-2)[0] in hvitebrikker:
                liste.append((x1+1,y1-2))
        except IndexError:
            pass
    elif get_piece(board,x,y)[0] == "♞":
        try:
            x1, y1 = x, y
            if get_piece(board,x1+2,y1-1)[0] == "_" or get_piece(board,x1+2,y1-1)[0] in svartebrikker:
                liste.append((x1+2,y1-1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1+2,y1+1)[0] == "_" or get_piece(board,x1+2,y1+1)[0] in svartebrikker:
                liste.append((x1+2,y1+1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-2,y1-1)[0] == "_" or get_piece(board,x1-2,y1-1)[0] in svartebrikker:
                liste.append((x1-2,y1-1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-2,y1+1)[0] == "_" or get_piece(board,x1-2,y1+1)[0] in svartebrikker:
                liste.append((x1-2,y1+1))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-1,y1+2)[0] == "_" or get_piece(board,x1-1,y1+2)[0] in svartebrikker:
                liste.append((x1-1,y1+2))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1+1,y1+2)[0] == "_" or get_piece(board,x1+1,y1+2)[0] in svartebrikker:
                liste.append((x1+1,y1+2))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1-1,y1-2)[0] == "_" or get_piece(board,x1-1,y1-2)[0] in svartebrikker:
                liste.append((x1-1,y1-2))
        except IndexError:
            pass
        try:
            x1, y1 = x, y
            if get_piece(board,x1+1,y1-2)[0] == "_" or get_piece(board,x1+1,y1-2)[0] in svartebrikker:
                liste.append((x1+1,y1-2))
        except IndexError:
            pass

    #dronning
    if get_piece(board,x,y)[0] == "♕":
        #springer bevegelse:
        #NØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1+1)[0] == "_" and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
                y1 += 1
                x1 += 1
            if get_piece(board,x1+1,y1+1)[0] in hvitebrikker and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
        except IndexError:
            pass
        #SØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1-1)[0] == "_" and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
                y1 -= 1
                x1 += 1
            if get_piece(board,x1+1,y1-1)[0] in hvitebrikker and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
        except IndexError:
            pass
        #SV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1-1)[0] == "_" and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
                y1 -= 1
                x1 -= 1
            if get_piece(board,x1-1,y1-1)[0] in hvitebrikker and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
        except IndexError:
            pass
        #NV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1+1)[0] == "_" and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
                y1 += 1
                x1 -= 1
            if get_piece(board,x1-1,y1+1)[0] in hvitebrikker and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
        except IndexError:
            pass
        #tårn bevegelse:
        # til venstre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1)[0] == "_" and x1 > 1:
                liste.append((x1-1,y1))
                x1 -= 1
            if get_piece(board,x1-1,y1)[0] in hvitebrikker and x1 > 1:
                liste.append((x1-1,y1))
        except IndexError:
            pass
        # til høyre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1)[0] == "_":
                liste.append((x1+1,y1))
                x1 += 1
            if get_piece(board,x1+1,y1)[0] in hvitebrikker:
                liste.append((x1+1,y1))
        except IndexError:
            pass
        # oppver
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1-1)[0] == "_" and y1 > 1:
                liste.append((x1,y1-1))
                y1 -= 1
            if get_piece(board,x1,y1-1)[0] in hvitebrikker and y1 > 1:
                liste.append((x1,y1-1))
        except IndexError:
            pass
        # nedover
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1+1)[0] == "_" and y1 < len(board):
                liste.append((x1,y1+1))
                y1 += 1
            if get_piece(board,x1,y1+1)[0] in hvitebrikker and y1 < len(board):
                liste.append((x1,y1+1))
        except IndexError:
            pass
    elif get_piece(board,x,y)[0] == "♛":
        #NØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1+1)[0] == "_" and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
                y1 += 1
                x1 += 1
            if get_piece(board,x1+1,y1+1)[0] in svartebrikker and y1 < len(board) and x1 < len(board):
                liste.append((x1+1,y1+1))
        except IndexError:
            pass
        #SØ
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1-1)[0] == "_" and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
                y1 -= 1
                x1 += 1
            if get_piece(board,x1+1,y1-1)[0] in svartebrikker and y1 > 1 and x1 < len(board):
                liste.append((x1+1,y1-1))
        except IndexError:
            pass
        #SV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1-1)[0] == "_" and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
                y1 -= 1
                x1 -= 1
            if get_piece(board,x1-1,y1-1)[0] in svartebrikker and y1 > 1 and x1 > 1:
                liste.append((x1-1,y1-1))
        except IndexError:
            pass
        #NV
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1+1)[0] == "_" and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
                y1 += 1
                x1 -= 1
            if get_piece(board,x1-1,y1+1)[0] in svartebrikker and y1 < len(board) and x1 > 1:
                liste.append((x1-1,y1+1))
        except IndexError:
            pass
        # til venstre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1-1,y1)[0] == "_" and x1 > 1:
                liste.append((x1-1,y1))
                x1 -= 1
            if get_piece(board,x1-1,y1)[0] in svartebrikker and x1 > 1:
                liste.append((x1-1,y1))
        except IndexError:
            pass
        # til høyre
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1+1,y1)[0] == "_":
                liste.append((x1+1,y1))
                x1 += 1
            if get_piece(board,x1+1,y1)[0] in svartebrikker:
                liste.append((x1+1,y1))
        except IndexError:
            pass
        # oppver
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1-1)[0] == "_" and y1 > 1:
                liste.append((x1,y1-1))
                y1 -= 1
            if get_piece(board,x1,y1-1)[0] in svartebrikker and y1 > 1:
                liste.append((x1,y1-1))
        except IndexError:
            pass
        # nedover
        x1 = x
        y1 = y
        try:
            while get_piece(board,x1,y1+1)[0] == "_" and y1 < len(board):
                liste.append((x1,y1+1))
                y1 += 1
            if get_piece(board,x1,y1+1)[0] in svartebrikker and y1 < len(board):
                liste.append((x1,y1+1))
        except IndexError:
            pass

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
    # hver gang du flytter en brikke måtte sjekke om kongen din er i sjakk også flytter man tilbake og printer at man ikke må sette sin egen konge i sjakk
    # mulig å sjekke hver brikke til en farge å se om kongens posisjon til den andre fargen er i legal moves til noen av brikkene, da er den i sjakk 
    pass

def sjekk_sjakk_matt(board):
    # lagre kongens posisjon, sjekk om sjekk_sjakk = true, så se om get_legal_moves returnerer tom liste.
    # mulig å bare bruke sjekk_sjakk()
    pass

def visbrett(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(f"{board[i][j]}", end=" ")
        print("",end="\n")
    print()


# board_string_1 = "...........................♕...................................."
board_string_1 = "♖♘♗♕♔♗♘♖♙♙♙♙♙♙♙♙................................♟♟♟♟♟♟♟♟♜♞♝♛♚♝♞♜"
#"♖, ♜, ♗, ♝, ♘, ♞, ♕, ♛, ♔, ♚, ♙, ♟"
board = make_board(board_string_1)


visbrett(board)
# print(get_piece(board,4,5))
# print(get_legal_moves(board,4,5))
move_piece(board,2,1,3,3)
visbrett(board)
move_piece(board,3,3,4,5)
visbrett(board)
move_piece(board,5,2,5,4)
visbrett(board)
move_piece(board,4,1,8,5)
visbrett(board)
move_piece(board,8,5,6,7)
visbrett(board)

# en while løkke for kjøring, hvor du sjekker om man er i sjakkmatt, eller sjakk, spørre om hvor du vil 
