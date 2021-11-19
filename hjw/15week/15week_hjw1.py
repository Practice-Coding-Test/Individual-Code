def solution(priorities, location):
    answer = 1
    docs = list(range(len(priorities)))
    while priorities:
        pri = priorities.pop(0)
        doc = docs.pop(0)
        if len(priorities) == 0:
            break
        if pri < max(priorities):
            priorities.append(pri)
            docs.append(doc)
        elif doc == location:
            break
        else:
            answer += 1
    return answer
