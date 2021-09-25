Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def solution(participant, completion):
    answer = ''
    tmp = 0
    dict = {}
    for i in participant:
        dict[hash(i)] = i
        tmp+= int(hash(i))
    for j in completion:
        tmp-= hash(j)
    answer = dict[tmp]
    return answer