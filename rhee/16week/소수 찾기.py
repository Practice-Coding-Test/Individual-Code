def s(n):
    answer = 0
    for i in range(2, n+1):
        cnt = 0
        for j in range(2, i+1):
            if i % j == 0:
                cnt += 1
                
        if cnt == 1:
            answer+=1
            
    return answer

def solution(n):
    # 에라토스테네스의 체
    a = [False,False] + [True]*(n-1)
    primes = []

    for i in range(2, n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    
    return len(primes)