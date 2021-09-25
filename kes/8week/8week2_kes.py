from collections import deque

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    prices = deque(prices) # 디큐로 넣기
    
    pre = prices.popleft() # 맨 처음 값 가져오기
    i=0

    while prices:
        cnt = 0
        for pre_idx, others in enumerate(prices):
            answer[i] += 1
            if((pre > others) or (pre_idx==len(prices)-1)): # 마지막이거나 가격이 떨어지면 조건문 들어가기
                pre = prices.popleft()
                i += 1 # 다음 날짜 기준으로 이동
                break

    return answer