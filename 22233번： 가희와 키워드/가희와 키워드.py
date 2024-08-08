#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 22233                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/22233                          #+#        #+#      #+#     #
#    Solved: 2024/08/06 13:22:12 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
import sys
input = sys.stdin.readline

keywordL, writeL = map(int, input().split())
keywords = {input().rstrip() : True for _ in range(keywordL)}

totalL = len(keywords)
for _ in range(writeL):
    words = input().rstrip().split(",")

    for word in words:
        if word in keywords:
            if keywords[word]:
                keywords[word] = False
                totalL -= 1
    print(totalL)