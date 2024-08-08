#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1182                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1182                           #+#        #+#      #+#     #
#    Solved: 2024/08/07 10:09:48 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
sys.setrecursionlimit(2**20)

n, s = map(int, input().split())
data = list(map(int, input().split()))
used = [False]*n
ans = 0
def backtracking(cur, arr):
    global ans
    
    if cur == n:
        if arr and sum(arr) == s:
            ans += 1
        return
    
    for i in range(2):
        if i == 0:
            backtracking(cur+1, arr + [data[cur]])
        else:
            backtracking(cur+1, arr)


    
backtracking(0, [])
print(ans)