N = int(input())
for i in range(N):
    r1x1, r1y1, r1x2, r1y2 = map(int, input().split())
    r2x1, r2y1, r2x2, r2y2 = map(int, input().split())
    
    # Finn minste og største x- og y-koordinater for det minste omsluttende rektangelet
    min_x = min(r1x1, r2x1)  # venstre side
    max_x = max(r1x2, r2x2)  # høyre side
    min_y = min(r1y1, r2y1)  # bunn
    max_y = max(r1y2, r2y2)  # topp
    
    # Beregn bredde og høyde for det omsluttende rektangelet
    bredde = max_x - min_x
    hoyde = max_y - min_y
    
    omkrets = 2 * (bredde + hoyde)
    
    print(omkrets)
    print(f"minx: {min_x}, maxx: {max_x}, miny: {min_y}, maxy: {max_y}")
    print(f"bredde: {bredde}, høyde: {hoyde}")
