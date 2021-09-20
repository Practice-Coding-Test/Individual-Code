import re
def solution(s):
    dic = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
    string = re.findall('[a-z]+',s)
    string = ''.join(string)
    for k,v in dic.items():
        if k in string:
            s = re.sub(k,str(v),s)

    answer =int(s)
    return answer