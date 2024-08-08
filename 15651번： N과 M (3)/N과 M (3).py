#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15651                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15651                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:30:05 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
used = [False] * (n+1)

def backTracking(arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
    
    for i in range(1, 1+n):
        backTracking(arr + [str(i)])

backTracking([])