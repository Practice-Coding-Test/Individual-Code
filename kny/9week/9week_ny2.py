# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

def solution(s):
    
    word, answer = [], []
    dic = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5'
      ,'six':'6','seven':'7','eight':'8','nine':'9'}
    
    for i in s:
        word.append(i)
        words = ''.join(word)
        if words in dic.keys():
            answer.append(dic.get(words))
            word = []
        elif str.isdigit(i):
            answer.append(i)
            word = []
    answer = int(''.join(answer))
    return answer
