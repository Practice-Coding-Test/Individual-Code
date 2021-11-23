def solution(n, words):
    answer = []
    past = []
    past.append(words[0])
    
    for i in range(1, len(words)):
        before = past[len(past)-1]
        bf_letter = before[len(before)-1]
        
        if words[i] in past or bf_letter != words[i][0]:
            answer.append(i%n+1) #사람 추가
            answer.append(int((i+1)/n+0.9)) # 번호 추가
            break
        past.append(words[i])
        
    if not answer:
        answer.append(0)
        answer.append(0)
        
    return answer
