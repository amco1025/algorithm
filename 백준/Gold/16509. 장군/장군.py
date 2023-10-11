def game(sx, sy, ex, ey, n):
    global ans

    if n >= ans:
        return

    if sx == ex and sy == ey:
        ans = min(ans, n)

    for di, dj in ((0,1),(1,0), (-1,0), (0,-1)):
        if 0 <= sx < 10 and 0 <= sy < 9:
            if sx != ex or sy != ey:
                sx += di
                sy += dj

                if di == 0 and dj == 1:
                    for dx, dy in ((-2,2),(2, 2)):
                        if 0<=sx+dx<10 and 0<=sy+dy<9:
                            if (sx+dx//2 != ex or sy+dy//2 != ey) and 0<=sx+dx//2<10 and 0<=sy+dy//2<9:
                                sx += dx
                                sy += dy
                                game(sx, sy, ex, ey, n+1)
                                sx = sx - dx
                                sy = sy - dy

                elif di == 0 and dj == -1:
                    for dx, dy in ((-2, -2), (2,-2)):
                        if 0<=sx+dx<10 and 0<=sy+dy<9:
                            if sx+dx//2 != ex or sy+dy//2 != ey and 0<=sx+dx//2<10 and 0<=sy+dy//2<9:
                                sx += dx
                                sy += dy
                                game(sx, sy, ex, ey, n+1)
                                sx = sx - dx
                                sy = sy - dy



                elif di == -1 and dj == 0:
                    for dx, dy in ((-2, -2), (-2, 2)):
                        if 0<=sx+dx<10 and 0<=sy+dy<9:
                            if sx+dx//2 != ex or sy+dy//2 != ey and 0<=sx+dx//2<10 and 0<=sy+dy//2<9:
                                sx += dx
                                sy += dy
                                game(sx, sy, ex, ey, n+1)
                                sx = sx - dx
                                sy = sy - dy




                elif di == 1 and dj == 0:
                    for dx, dy in ((2, -2), (2, 2)):
                        if 0<=sx+dx<10 and 0<=sy+dy<9:
                            if sx+dx//2 != ex or sy+dy//2 != ey and 0<=sx+dx//2<10 and 0<=sy+dy//2<9:
                                sx += dx
                                sy += dy
                                game(sx, sy, ex, ey, n+1)
                                sx = sx - dx
                                sy = sy - dy
                sx -= di
                sy -= dj


start = list(map(int, input().split()))
end = list(map(int, input().split()))

ans = 10

game(start[0], start[1], end[0], end[1], 0)

if ans == 10:
    print(-1)
else:
    print(ans)
