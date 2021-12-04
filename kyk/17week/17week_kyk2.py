
#프로그래머스 코딩테스트 연습
#Summer/Winter Coding(~2018)
#소수 만들기 

from itertools import combinations

def check(num):
    for i in range(2,num):
        if num % i == 0:
            return 0
    return num

def solution(nums):
    temp, answer= list(combinations(nums, 3)), []
    for t in temp:
        result= check(sum(t))
        if result != 0:
            answer.append(result)

    return len(answer)
