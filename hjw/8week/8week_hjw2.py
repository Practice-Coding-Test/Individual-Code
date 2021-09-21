from collections import Counter
def multiplyList(myList) :
    result = 1
    for x in myList:
         result = result * x
    return result

def solution(clothes):
    answer = 1
    result = []
    kind = Counter([c[1] for c in clothes]).values() # 주어진 옷들의 종류별 count
    result = [n+1 for n in list(kind)] # 조합 = (종류a+1)*(종류b+1)* ... - 1이므로 각 종류에 +1한 수치 구현
    return multiplyList(result)-1