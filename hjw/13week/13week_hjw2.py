import math
def solution(progresses, speeds):
    answer = []
    temp = []
    lst = []
    max_prog = 0
    max_idx = 0
    for i in range(len(progresses)):
        answer.append(math.ceil((100-progresses[i]) / speeds[i]))
    for idx, ans in enumerate(answer):
        if ans > max_prog:
            max_prog = ans
            temp.append(idx)
    temp.append(len(answer))
    for t in range(1,len(temp)):
        lst.append(temp[t]-temp[t-1])
    return lst
