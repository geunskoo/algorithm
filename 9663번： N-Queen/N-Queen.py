#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 9663                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/9663                           #+#        #+#      #+#     #
#    Solved: 2024/08/07 09:39:53 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

N = int(input())

colUsed = [False] * (N)
crossUsed = [False] * (2*N-1)
rcrossUsed = [False] * (2*N-1) 

ans = 0
def nQueen(row):
    global ans
    if row == N:
        ans += 1
    
    for i in range(N):
        if colUsed[i] or crossUsed[i+row] or rcrossUsed[i-row+N-1]:
            continue
        colUsed[i] = True
        crossUsed[i+row] = True
        rcrossUsed[i-row+N-1] = True
        nQueen(row+1)
        colUsed[i] = False
        crossUsed[i+row] = False
        rcrossUsed[i-row+N-1] = False

nQueen(0)
print(ans)
