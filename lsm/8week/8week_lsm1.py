# �ֽİ���
def solution(prices):
    answer = [0] * len(prices) # prices ���̸�ŭ 0 ����Ʈ ����
    for i in range(len(prices)-1): # (prices ����-1)��ŭ �ݺ� / �������� ���� �� ����
        for j in range(i+1, (len(prices))): # i+1 ~ prices ���̸�ŭ �ݺ�
            answer[i] += 1 # ������ �������� ������ +1
            if (prices[i] > prices[j]): # ������ �������� break
                break
    return answer