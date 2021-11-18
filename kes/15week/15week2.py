def solution(priorities, location):
    from collections import deque

    Q = []
    for i, v in enumerate(priorities):
        Q.append((v, i))
    Q = deque(Q)
    cnt = 0
    while True:
        cur = Q.popleft()
        if any(cur[0] < x[0] for x in Q):
            Q.append(cur)
        else:
            cnt += 1
            if cur[1] == location:
                return cnt
