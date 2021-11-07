def solution(absolutes, signs):
    final = 0
    real = []
    for i in signs:
        if i == True:
            real.append(1)
        else:
            real.append(-1)
    for i in range(len(absolutes)):
        final+=absolutes[i]*real[i]
    return final








