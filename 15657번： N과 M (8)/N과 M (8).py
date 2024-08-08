#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15657                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15657                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:58:21 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def backTracking(prev, arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
    
    for i in range(len(data)):
        if prev <= data[i]:
            backTracking(data[i], arr + [str(data[i])])

backTracking(-1, [])