#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2531                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2531                           #+#        #+#      #+#     #
#    Solved: 2024/08/10 09:04:04 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

INITIAL_VALUE = -1
#프로세스
def solution(n, d, k, c, sushi):
    round_sushi = sushi + sushi[:k]

    maxValue = INITIAL_VALUE
    for start_index in range(n):
        maxValue = max(maxValue, len(set(round_sushi[start_index : start_index+k] + [c])))

    print(maxValue)



#입력
n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]
solution(n, d, k, c, sushi)




