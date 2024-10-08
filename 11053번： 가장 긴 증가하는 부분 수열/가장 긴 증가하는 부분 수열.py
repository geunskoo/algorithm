#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 11053                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/11053                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 10:58:36 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
data = list(map(int, input().split()))

dp = [1]*n

for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))