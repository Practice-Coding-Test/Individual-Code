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


import numpy as np

def solution(scores):
    scores = np.array(scores)
    answer = []
    
    for i in range(len(scores)):
        x = scores[:,i]
        y = np.delete(x,i)
        if (min(x) == x[i]) | (max(x) == x[i]):
            if x[i] not in y:
                x = y
        average = x.mean()
        print(x)
    
        if average>=90:
            answer.append('A')
        elif 80<=average<90:
            answer.append('B')
        elif 70<=average<80:
            answer.append('C')
        elif 50<=average<70:
            answer.append('D')
        else:
            answer.append('F')
    
    answer = ''.join(answer)
    return answer




solution(scores)
