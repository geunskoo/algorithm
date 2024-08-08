#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15650                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15650                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:18:10 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
used = [False] * (n+1)

def backTracking(index, arr):
    if len(arr) == m:
        print(' '.join(arr))
        return
    
    for candidate in range(1, n+1):
        if not used[candidate] and index < candidate:
            used[candidate] = True
            backTracking(candidate, arr + [str(candidate)])
            used[candidate] = False

backTracking(0, [])