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

# +
import numpy as np

key = {1: [0,0],2: [0,1],3: [0,2],
       4: [1,0],5: [1,1],6: [1,2],
       7: [2,0],8: [2,1],9: [2,2],
       10: [3,0],0: [3,1],11: [3,2]}
ans, right, left = [], 11, 10

def solution(numbers, hand):
    global key, ans, right, left
    for i in range(len(numbers)):
        if numbers[i] in [1,4,7]:
            left = numbers[i]
            ans.append('L')

        elif numbers[i] in [3,6,9]:
            right = numbers[i]
            ans.append('R')

        else:
            arr_right = np.sum(np.abs(np.array(key.get(right))-np.array(key.get(numbers[i]))))
            arr_left = np.sum(np.abs(np.array(key.get(left))-np.array(key.get(numbers[i]))))
            if arr_right == arr_left:
                if hand == 'right':
                    right = numbers[i]
                    ans.append('R')
                else:
                    left = numbers[i]
                    ans.append('L')
            elif arr_right < arr_left:
                right = numbers[i]
                ans.append('R')
            else:
                left = numbers[i]
                ans.append('L')
    answer = ''.join(ans)
    return answer


# -

solution(numbers,hand)
