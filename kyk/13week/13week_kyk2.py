#프로그래머스 코딩테스트 연습
#완전탐색
#모의고사


def solution(answers):
    student1= [1,2,3,4,5]
    student2= [2,1,2,3,2,4,2,5]
    student3= [3,3,1,1,2,2,4,4,5,5]
    q, score, result= 0, {1:0, 2:0, 3:0}, []
    
    for answer in answers:
        q += 1
        if student1[q%5-1] == answer:
            score[1] += 1
        if student2[q%8-1] == answer:
            score[2] += 1
        if student3[q%10-1] == answer:
            score[3] += 1
    
    high= max(list(score.values()))
    for i in range (1,4):
        if high == score[i]:
            result.append(i)

    return result