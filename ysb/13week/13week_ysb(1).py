def solution(numbers):
    total_num = [i for i in range(0,10)]
    a = [i for i in total_num if i not in numbers]
    return sum(a)