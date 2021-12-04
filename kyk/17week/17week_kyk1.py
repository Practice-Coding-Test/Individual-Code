
#프로그래머스 코딩테스트 연습
#2021 Dev-Matching: 웹 백엔드 개발자(상반기)
#로또의 최고 순위와 최저 순위

def solution(lottos, win_nums):
    cnt,zero,answer=0,0,[]
    score=[6,6,5,4,3,2,1]
    for lotto in lottos:
        if lotto == 0:
            zero += 1
        if lotto in win_nums:
            cnt += 1

    answer.append(score[zero+cnt])
    answer.append(score[cnt])

    return answer