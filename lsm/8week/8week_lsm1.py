# 주식가격
def solution(prices):
    answer = [0] * len(prices) # prices 길이만큼 0 리스트 생성
    for i in range(len(prices)-1): # (prices 길이-1)만큼 반복 / 마지막은 비교할 수 없음
        for j in range(i+1, (len(prices))): # i+1 ~ prices 길이만큼 반복
            answer[i] += 1 # 가격이 떨어지지 않으면 +1
            if (prices[i] > prices[j]): # 가격이 떨어지면 break
                break
    return answer