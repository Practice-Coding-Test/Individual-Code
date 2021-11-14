def solution(n, lost, reserve):
    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    for x in lost:
        if x in reserve:
            answer += 1
            reserve.remove(x)
        elif x - 1 in reserve:
            answer += 1
            reserve.remove(x-1)
        elif x + 1 in reserve and x+1 not in lost:
            answer += 1
            reserve.remove(x + 1)
    return answer
