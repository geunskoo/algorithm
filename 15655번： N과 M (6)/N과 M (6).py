#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15655                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15655                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:48:01 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
used = [False] * n

def backTracking(prev, arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
    
    for i in range(len(data)):
        if not used[i] and prev < data[i]:
            used[i] = True
            backTracking(data[i], arr + [str(data[i])])
            used[i] = False

backTracking(-1, [])