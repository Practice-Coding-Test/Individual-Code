def solution(n, lost, reserve):
    answer = 0
    for i in range(1,n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    for i in range(1, n+1):
        if i in lost:
            if (i-1) in reserve:
                reserve.remove(i-1)
                lost.remove(i)
            elif (i+1) in reserve:
                reserve.remove(i+1)
                lost.remove(i)
                print(i)
    return n-len(lost)
