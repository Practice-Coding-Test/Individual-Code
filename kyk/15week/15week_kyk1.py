#월간 코드 챌린지 시즌2
#음양 더하기

def solution(absolutes, signs):

    for i in range(len(signs)):
        if signs[i] == False:
            absolutes[i]= absolutes[i]*-1

    return sum(absolutes)