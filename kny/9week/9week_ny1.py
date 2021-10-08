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

def solution(lottos,win_nums):
    count0 = lottos.count(0)
    lottos_remove0 = [item for item in lottos if item != 0]
    min_correct = 6-len(list(set(win_nums)-set(lottos_remove0)))
    max_correct = min_correct + count0
    rank = {6:1,5:2,4:3,3:4,2:5,1:6,0:6}
    answer = [rank.get(max_correct),rank.get(min_correct)]
    return answer
