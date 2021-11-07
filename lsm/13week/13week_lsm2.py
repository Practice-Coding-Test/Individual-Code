def solution(d, budget):
    count = 0
    temp = []
    for i in range(len(d)):
        temp.append(min(d))
        d.remove(min(d))
        count += 1
        if sum(temp) > budget:
            count -= 1
            break
    return count