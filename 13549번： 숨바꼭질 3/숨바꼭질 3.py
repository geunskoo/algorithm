#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 13549                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/13549                          #+#        #+#      #+#     #
#    Solved: 2024/08/08 14:03:11 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq
INF = int(1e9)

def moveAndCost(index, val):
    if index == 0:
        return val + 1, 1
    elif index ==1:
        return val - 1, 1
    else:
        return 2*val, 0

def solution(N, K):
    
    costs = [INF] * 100001
    heap = []
    heapq.heappush(heap, (0, N))
    costs[N] = 0
    while heap:
        cost, x = heapq.heappop(heap)
        for i in range(3):
            nx, nextCost = moveAndCost(i, x)
            if nx < 0 or nx > 100000:
                continue
            if costs[nx] > cost + nextCost:
                costs[nx] = cost + nextCost
                heapq.heappush(heap, (cost + nextCost, nx))
    print(costs[K])

N, K = map(int, input().split())
solution(N, K)