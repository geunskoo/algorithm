#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1504                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1504                           #+#        #+#      #+#     #
#    Solved: 2024/08/07 11:51:16 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import defaultdict
import heapq

nodeN, edgeN = map(int, input().split())
connectness = defaultdict(list)
for _ in range(edgeN):
    start, end, cost = map(int, input().split())
    connectness[start].append([cost, end])
    connectness[end].append([cost, start])
nodeA, nodeB = map(int, input().split())


def dijkstra(connectness, start, target):
    costs = [int(1e9)] * (nodeN+1)
    heap = []

    costs[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        cost, node = heapq.heappop(heap)

        if node == target:
            return cost
        
        for nextCost, nextNode in connectness[node]:
            if costs[nextNode] > cost + nextCost:
                costs[nextNode] = cost + nextCost
                heapq.heappush(heap, (cost+nextCost, nextNode))
    return int(1e9)

def solution(connectness, nodeA, nodeB):
    case1 = dijkstra(connectness, 1, nodeA) + dijkstra(connectness, nodeA, nodeB) + dijkstra(connectness, nodeB, nodeN)
    case2 = dijkstra(connectness, 1, nodeB) + dijkstra(connectness, nodeB, nodeA) + dijkstra(connectness, nodeA, nodeN)
    
    return min(case1, case2) if min(case1, case2) < int(1e9) else -1




answer = solution(connectness, nodeA, nodeB)
print(answer)