#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2512                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2512                           #+#        #+#      #+#     #
#    Solved: 2024/08/06 12:33:16 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

#입력
n = int(input())
requestMoneys = list(map(int, input().split()))
cMoney = int(input())

def calculateMoney():
    stdMoney = 0
    prevMaxMoney = 0
    while True:
        maxMoney = - 1
        total = 0
        for money in requestMoneys:
            if stdMoney > money:
                if maxMoney < money:
                    maxMoney = money
                total += money
            else:
                if maxMoney < stdMoney:
                    maxMoney = stdMoney
                total += stdMoney
            
            if total > cMoney:
                return prevMaxMoney
            
        prevMaxMoney = maxMoney
        stdMoney += 1


answer = 0
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
if sum(requestMoneys) <= cMoney:
    answer = max(requestMoneys)

# 2. 모든 요청이배정될 수 없는 경우 특정한 상한액을 계산하여 준다.
else:
    answer = calculateMoney()

print(answer)