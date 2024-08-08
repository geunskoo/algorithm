#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15654                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15654                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:38:52 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
used = [False] * n

def backTracking(arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
    
    for i in range(len(data)):
        if not used[i]:
            used[i] = True
            backTracking(arr + [str(data[i])])
            used[i] = False

backTracking([])