# ��ȭ��ȣ ���
def solution(phone_book):
    judge = True # boolean���� �Ǵ�
    temp = sorted(phone_book) # phone_book�� ������������ ����
    for i in range(len(temp)-1): # temp���̸�ŭ �ݺ�/���⼭ -1�� ������ ���� �� ����
        if temp[i] in temp[i+1]: # �տ� ���� �ڿ� ���� ���ϸ� = ���ξ�
            judge = False # False
    return judge