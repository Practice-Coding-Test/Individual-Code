def solution(people, limit):
    answer = 0
    people = sorted(people)
    l_cnt = 0
    h_cnt = len(people)-1
    while h_cnt - l_cnt > 0:
        if people[l_cnt]+people[h_cnt] <= limit:
            l_cnt += 1
            h_cnt -= 1
        else:
            h_cnt -= 1
        answer += 1
        if h_cnt == l_cnt:
            answer += 1
    return answer
