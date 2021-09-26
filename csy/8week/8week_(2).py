def solution(word):
    al = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    answer = len(word) # A를 0으로 두었기 때문에 길이로 초기화
    w = (((5 + 1) * 5 + 1) * 5 + 1) * 5 + 1 # 781
    
    for i in word:
        answer += w * al[i] # 시작하는 첫 문자
        w = (w - 1) // 5
        
    return answer
