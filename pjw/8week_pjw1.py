#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(board, moves):
    new_board = list(map(list, zip(*board)))
    list1 = []
    for m in moves:
        for i in range(len(board)):
            if new_board[m-1][i] == 0:
                pass
            else:
                list1.append(new_board[m-1][i])
                new_board[m-1][i] = 0
                break
    answer = 0
    for k in range(len(list1)-1):
        if list1[k] == list1[k+1]:
            answer += 2
            if list1[k-1] == list1[k+2]:
                answer += 2
            else:
                pass
         
    
    return answer

