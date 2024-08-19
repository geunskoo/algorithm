#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20125                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20125                          #+#        #+#      #+#     #
#    Solved: 2024/08/19 13:38:25 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def findHead(N, cookieImage):
    for x in range(N):
        for y in range(N):
            if cookieImage[x][y] == '*':
                return x, y

def findArmLength(heartX, heartY, cookieImage):

    leftIndex = "".join(cookieImage[heartX]).find('*')
    rightIndex = "".join(cookieImage[heartX]).rfind('*')
    
    return heartY - leftIndex, rightIndex - heartY
        
def findEndWaistAndLength(heartX, heartY, N, cookieImage):
    waistLength = 0
    for x in range(heartX+1, N):
        if cookieImage[x][heartY] == '*':
            waistLength += 1
        else:
            return x-1, heartY, waistLength
        
def findLegLength(waistX, waistY, N, cookieImage):
    startLegX = waistX + 1
    leftLegY = waistY - 1
    rightLegY = waistY + 1
    leftLeg = 0
    rightLeg = 0
    for x in range(startLegX, N):
        if cookieImage[x][leftLegY] == '*':
            leftLeg += 1
        
        if cookieImage[x][rightLegY] == '*':
            rightLeg += 1

    return leftLeg, rightLeg

def solution(N, cookieImage):
    #머리 좌표
    headX, headY = findHead(N, cookieImage)
    #심장 좌표
    heartX, heartY = headX + 1, headY 

    #팔길이
    leftArm, rightArm = findArmLength(heartX, heartY, cookieImage)

    #허리길이
    waistX, waistY, waist = findEndWaistAndLength(heartX, heartY, N, cookieImage)

    leftLeg, rightLeg = findLegLength(waistX, waistY, N, cookieImage)

    print(heartX+1, heartY+1)
    print(leftArm, rightArm, waist, leftLeg, rightLeg)

N = int(input())
cookieImage = [list(input()) for i in range(N)]
solution(N, cookieImage)