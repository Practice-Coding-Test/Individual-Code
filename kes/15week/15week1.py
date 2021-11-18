def solution(progresses, speeds):
    cnt = 1
    answer = []
    
    on_going = int((100 - progresses[0]) / speeds[0] + 0.9)
    for i in range(1, len(progresses)):
        tmp = int((100 - progresses[i]) / speeds[i] + 0.9)
        if on_going >= tmp:
            cnt += 1
        else:
            answer.append(cnt)
            on_going = tmp
            cnt = 1
    answer.append(cnt)

    return answer
