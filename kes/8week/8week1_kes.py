def solution(cite):
    answer = 0
    cite.sort(reverse=True) # 역순으로 정렬 하기

    for h in range(cite[0], 0, -1): # 최댓값 부터 계산
        if (len(cite) >= h) and (cite[h-1] >= h): # 인용수 조건 만족 여부 판단
            answer = h
            break

    return answer
