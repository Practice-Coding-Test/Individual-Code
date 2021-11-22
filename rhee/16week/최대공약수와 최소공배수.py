def solution(n, m):
    n, m =  min(n, m), max(n, m)

    mul = n * m
    
    while m:
        n, m = m, n % m
    
    return [n, mul // n]