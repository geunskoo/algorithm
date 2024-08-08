#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 14719                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/14719                          #+#        #+#      #+#     #
#    Solved: 2024/08/06 15:32:42 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

# 입력
y, x = map(int, input().split())
heights = list(map(int, input().split()))
graph = [[0] * y for _ in range(x)]

#기둥 세우기
for i in range(x):
    for j in range(heights[i]):
        graph[i][j] = 1

#물채우기

totalHap = 0
for height in range(y):
    hap = 0
    prevStart = -1
    for width in range(x):
        if graph[width][height] == 1:
            start = width
            if prevStart  == -1:
                prevStart = start
            else:
               hap += (start - prevStart - 1)
               prevStart = start          
    totalHap += hap
print(totalHap)