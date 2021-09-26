#5637 가장 긴 단어
#영문이나 -이면 카운트 업, 단어끝나면 맥스값 체크해서 갱신 
#문자열의 구성이 알파벳 or 한글인지 확인하는 방법 [isalpha] 
#숫자인지 확인하는 방법 [isdigit]
#알파벳(한글) 또는 숫자인지 확인하는법[isalnum]
import sys

max_ = 0
cnt = 0
while True:
    inputdata= input().split() 

    for word in inputdata: 
        if word != 'E-N-D':
            cnt = 0
            for i in word:
                if i.isalpha() or i == '-': 
                    cnt += 1

        if max_ < cnt: 
            answer = word 
            max_ = cnt
        else: 
            break
print(answer.lower())