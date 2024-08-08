#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4485                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4485                           #+#        #+#      #+#     #
#    Solved: 2024/08/07 11:12:57 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import heapq

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def solution(n, graph):
    heap = []
    costs = [[1e9] * n for _ in range(n)]

    costs[0][0] = graph[0][0]
    heapq.heappush(heap, (graph[0][0], 0, 0))
    
    while heap:
        cost, x, y = heapq.heappop(heap)

        if x == n-1 and y == n-1:
            return cost
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                continue

            newCost = cost + graph[nx][ny]
            if costs[nx][ny] > newCost:
                costs[nx][ny] = newCost
                heapq.heappush(heap, (newCost, nx, ny))

problem = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    value = solution(n, graph)
    print(f'Problem {problem}: {value}')
    problem += 1