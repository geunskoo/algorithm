#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20437                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20437                          #+#        #+#      #+#     #
#    Solved: 2024/08/06 13:56:23 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import defaultdict

def setUpChecker(word, sildeSize):
    checker = defaultdict(int)
    for i in range(sildeSize):
        checker[word[i]] += 1
    return checker

def searchTarget(checker, targetNum):
    for key in checker:
        if checker[key] == targetNum:
            return True
    return False

def findShortestWord(word, targetNum):
    for sildeSize in range(targetNum, len(word)+1):
        #슬라이드 윈도우 크기 정함
        checker = setUpChecker(word, sildeSize)
        if searchTarget(checker,targetNum):
            return sildeSize
        for index in range(1, len(word)-sildeSize):
            #슬라이드 윈도우 움직이는 곳
            
            checker[word[index+sildeSize-1]] += 1
            checker[word[index-1]] -= 1
            if searchTarget(checker, targetNum):
                return sildeSize
    return -1
            
def findLongestWord(word, targetNum):
    for sildeSize in range(len(word), targetNum-1, -1):
        #슬라이드 윈도우 크기 정함
        checker = setUpChecker(word, sildeSize)
        if searchTarget(checker, targetNum) and word[0] == word[sildeSize-1]:
            return sildeSize
        for index in range(1, len(word)-sildeSize):
            #슬라이드 윈도우 움직이는 곳
            checker[word[index+sildeSize-1]] += 1
            checker[word[index-1]] -= 1

            if searchTarget(checker, targetNum) and word[index] == word[index+sildeSize]:
                return sildeSize
    return -1

#프로세스
def process(word, targetNum):

    answer1 = findShortestWord(word, targetNum)
    answer2 = findLongestWord(word, targetNum)
    
    if answer1 == -1 or answer2 == -1:
        print(-1)
    else:
        print(answer1, answer2)    


#입력
t = int(input())
for _ in range(t):
    word = input()
    targetNum = int(input())
    process(word, targetNum)