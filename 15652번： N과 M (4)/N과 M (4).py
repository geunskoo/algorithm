#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15652                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15652                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:34:54 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())

def backTracking(index, arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
    
    for i in range(1, 1+n):
        if index <= i:
            backTracking(i, arr + [str(i)])

backTracking(0, [])