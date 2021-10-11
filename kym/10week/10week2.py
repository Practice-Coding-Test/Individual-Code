def solution(answers):
    length = len(answers)
    one = [1,2,3,4,5]
    rep_num1 = (length//len(one) +1)
    two = [ 2, 1, 2, 3, 2, 4, 2, 5]
    rep_num2 = (length//len(two) +1)
    three = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    rep_num3 = (length//len(three) +1)
    new_one,new_two,new_three = one*rep_num1, two * rep_num2, three*rep_num3
    x,y,z = new_one[:length],new_two[:length],new_three[:length]
    score1,score2,score3 =0,0,0
    
    for a,i,j,k in zip(answers,x,y,z):
        if a == i: score1 += 1
        if a == j: score2 += 1
        if a == k : score3 += 1
    ls = [score1,score2,score3]
    answer = []
    for i,k in enumerate(ls):
        if k == max(ls):
            answer.append(i+1)
        
    
    return answer

print(solution([1,3,2,4,2]))