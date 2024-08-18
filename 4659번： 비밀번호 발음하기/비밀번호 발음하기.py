#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 4659                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: geunskoooo <boj.kr/u/geunskoooo>            +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/4659                           #+#        #+#      #+#     #
#    Solved: 2024/08/18 18:34:34 by geunskoooo    ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

def solution(password):
    moum = ['a', 'e', 'i', 'o', 'u']
    allowDouble = ['e', 'o']
    moumIndexes = []
    prevChar = '-'
    for index, c in enumerate(password):
        if c in moum:
            moumIndexes.append(index)
        
        if prevChar == c and c not in allowDouble:
            return False
        prevChar = c

    if not moumIndexes:
        return False
    
    if moumIndexes[0] >= 3:
        return False
    
    if moumIndexes[-1] + 4 <= len(password):
        return False
    
    prev = moumIndexes[0]
    for i in range(1, len(moumIndexes)):
        if (prev + 4) <=  moumIndexes[i]:
            return False
        prev = moumIndexes[i]

    moumStack = 1
    prevIndex = moumIndexes[0]
    for i in range(1, len(moumIndexes)):
        if prevIndex + 1 ==  moumIndexes[i]:
            moumStack += 1
            if moumStack == 3:
                return False
        else:
            moumStack = 1

        prevIndex = moumIndexes[i]

    return True

while True:
    password = input()
    if password == 'end':
        break
    acceptable = solution(password)

    if acceptable:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
