#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15656                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15656                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 01:52:29 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n, m = map(int, input().split())
data = list(map(int, input().split()))
data.sort()

def backTracking(arr):
    if len(arr) == m:
        print(' '.join(arr))
        return 
    
    for i in range(len(data)):
        backTracking( arr + [str(data[i])])

backTracking([])