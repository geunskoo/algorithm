def swapX(game, x, y):
    game[x][y], game[x+1][y] = game[x+1][y], game[x][y] 

def swapY(game, x, y):
    game[x][y+1], game[x][y] = game[x][y], game[x][y+1] 

def findMaxCandy(game, n):
    candys = []
    for x in range(n):
        for y in range(n):
            #rowCheck
            stdCandy = game[x][y]
            candyLen = 1
            for nx in range(x+1, n):
                if stdCandy == game[nx][y]:
                    candyLen += 1
                    if nx == n-1:
                        candys.append(candyLen)
                else:
                    candys.append(candyLen)
                    break
            

            #colCheck
            candyLen = 1
            for ny in range(y+1, n):
                if stdCandy == game[x][ny]:
                    candyLen += 1
                    if ny == n-1:
                        candys.append(candyLen)
                else:
                    candys.append(candyLen)
                    break
        
    return max(candys)

def solution(game, n):
    maxCandy = -1
    for x in range(n):
        for y in range(n):
            #swap x
            if x != n-1:     
                swapX(game, x, y)
                maxCandy = max(maxCandy, findMaxCandy(game, n))
                swapX(game, x, y)
                
            #swap y
            if y != n-1:
                swapY(game, x, y)
                maxCandy = max(maxCandy, findMaxCandy(game, n))
                swapY(game, x, y)

    print(maxCandy)


#입력
n = int(input())
game = [list(input()) for _ in range(n)]
solution(game, n)