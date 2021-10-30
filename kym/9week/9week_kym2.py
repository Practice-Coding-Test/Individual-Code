from itertools import combinations
def solution(numbers):
    prob = list(combinations(numbers,2))
    answer = sorted(set([i+j for i,j in prob]))
    return answer