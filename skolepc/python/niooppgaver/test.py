N = int(input())

for i in range(N):
    r1x1, r1y1, r1x2, r1y2 = map(int, input().split())
    r2x1, r2y1, r2x2, r2y2 = map(int, input().split())

    min_x = min(r1x1,r1x2,r2x1,r2x2)
    max_x = max(r1x1,r1x2,r2x1,r2x2)
    min_y = min(r1y1,r1y2,r2y1,r2y2)
    max_y = max(r1y1,r1y2,r2y1,r2y2)

    bredde = max_x - min_x
    hoyde = max_y - min_y

    print(2*(bredde + hoyde))