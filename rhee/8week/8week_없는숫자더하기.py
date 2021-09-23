def solution(numbers):
    answer = 0
    for j in range(10):
        if j not in numbers:
            answer += j
    return answer