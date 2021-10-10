def solution(d, budget):
    answer = 0
    d.sort() # d 정렬 : 많은 부서에 물품을 지원하기 위해서는 신청금액이 적은 부서부터 지원해야 하므로
    
    for i in range(len(d)): 
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
            
    return answer
