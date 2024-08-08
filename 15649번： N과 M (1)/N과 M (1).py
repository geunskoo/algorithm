#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15649                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15649                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:07:56 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
used = [False] * (n+1)
def backTracking(arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
        
    for i in range(1, n+1):
        if not used[i]:
            used[i] = True
            backTracking(arr + [str(i)])
            used[i] = False

backTracking([])