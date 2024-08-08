#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20437                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20437                          #+#        #+#      #+#     #
#    Solved: 2024/08/06 15:30:11 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import defaultdict

# 프로세스
def process(word, num):
    alphaIndexes = defaultdict(list)
    findFlag = False
    for index, c in enumerate(word):
        if word.count(c) >= num:
            alphaIndexes[c].append(index)
            findFlag = True

    if not findFlag:
        return -1, -1

    maxValue, minValue = -1, 10001 
    for alpha in alphaIndexes:
        indexes = alphaIndexes[alpha]
        for i in range(len(indexes) - num + 1):
            candidateValue = indexes[i+num-1] - indexes[i] + 1
            maxValue = max(maxValue, candidateValue)
            minValue = min(minValue, candidateValue)

    return maxValue, minValue

#입력
T = int(input())
for i in range(T):
    word = input()
    num = int(input())
    maxValue, minValue = process(word, num)
    
    if maxValue == -1:
        print(-1)
    else:
        print(minValue, maxValue)