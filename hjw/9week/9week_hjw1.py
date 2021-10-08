def solution(citations):
    answer = 0
    for i, v in enumerate(list(sorted(citations, reverse=True))):
        if i >= v:
            answer = i
            break
        else:
            answer = len(citations)
    return answer
