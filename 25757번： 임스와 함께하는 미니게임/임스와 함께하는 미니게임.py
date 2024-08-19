#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 25757                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/25757                          #+#        #+#      #+#     #
#    Solved: 2024/08/19 13:12:55 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def getPlayerNum(playType):
    if playType == 'Y':
        return 1
    elif playType == 'F':
        return 2
    elif playType == 'O':
        return 3

def solution(gameType, participants):
    
    playedPerson = set()
    waittingRoom = []
    playCount = 0
    playerNum = getPlayerNum(gameType)
    for person in participants:
        if person in playedPerson:
            continue

        waittingRoom.append(person)
        playedPerson.add(person)
        if len(waittingRoom) == playerNum:
            waittingRoom = []
            playCount += 1

    return playCount


n, gameType = input().split()
gameNum = int(n)
participants = [input() for i in range(gameNum)]
answer = solution(gameType, participants)
print(answer)