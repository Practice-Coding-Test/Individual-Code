#프로그래머스 코딩테스트 연습
#2021 카카오 채용연계형 인턴십
#숫자 문자열과 영단어

def solution(s):
    word= [ 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
    num= ['0','1','2','3','4','5','6','7','8','9']

    answer, temp= '', ''
    for i in s:
        if i in num:
            answer += i
        else:
            temp += i
            if temp in word:
                answer += str(word.index(temp))
                temp= ''
    return int(answer)
