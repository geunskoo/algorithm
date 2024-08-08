#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 20006                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/20006                          #+#        #+#      #+#     #
#    Solved: 2024/08/07 00:07:55 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import defaultdict

def solution(p, m, data):
    # 방 목록
    rooms = []

    def newRoom(level, name):
        room = []
        room.append([level, name])
        return room

    for level, name in data:

        if not rooms:
            room = newRoom(level, name)
            rooms.append(room)
            continue
        
        isEnterRoom = False
        for room in rooms:
            stdLevel = room[0][0]
            if stdLevel-10 <= level and level <= stdLevel+10 and len(room) < m:
                
                room.append([level, name])
                isEnterRoom = True
                break

        if not isEnterRoom:
            room = newRoom(level, name) 
            rooms.append(room)
    
    return rooms


p, m = map(int, input().split())

data = []
for i in range(p):
    level, name = input().split()
    data.append([int(level), name])
rooms = solution(p, m, data)

for room in rooms:
    if len(room) == m:
        print("Started!")
    else:
        print("Waiting!")
    room.sort(key=lambda x: x[1])
    for level, name in room:
        print(level, name)

