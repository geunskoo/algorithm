#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2075                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2075                           #+#        #+#      #+#     #
#    Solved: 2024/08/10 09:03:53 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())

# 5 7 9 12 15

heap = []
for _ in range(n):
    for v in map(int, input().rstrip().split()):
        if len(heap) < n:
            heapq.heappush(heap, v)
        else:
            if v > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, v)

print(heap[0])

