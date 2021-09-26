# 전화번호 목록
def solution(phone_book):
    judge = True # boolean으로 판단
    temp = sorted(phone_book) # phone_book을 오름차순으로 정렬
    for i in range(len(temp)-1): # temp길이만큼 반복/여기서 -1은 마지막 연산 때 오류
        if temp[i] in temp[i+1]: # 앞에 값이 뒤에 값에 속하면 = 접두어
            judge = False # False
    return judge