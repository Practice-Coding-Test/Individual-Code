def solution(numbers, target):
    global answer
    answer = 0
    DFS(0, 0, numbers, target)
    return answer

def DFS(L, sum, numbers, target):
    global answer
    if L>=len(numbers):
        if sum == target:
            answer += 1
        return
    else:
        DFS(L + 1, sum + numbers[L], numbers, target)
        DFS(L + 1, sum - numbers[L], numbers, target)