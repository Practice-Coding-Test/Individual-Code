def DFS(now, cnt, ch, target, words):
    global answer
    if now == target:
        if cnt < answer:
            answer = cnt
        return
    else:
        for i in range(len(words)):
            stop = 0
            for j in range(len(target)):
                if now[j] != words[i][j]:
                    stop += 1
            if stop == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(words[i], cnt+1, ch, target, words)
                ch[i] = 0

def solution(begin, target, words):
    global answer
    answer = 21470000
    ch = [0]*len(words)
    DFS(begin, 0, ch, target, words)
    if answer == 21470000:
        return 0
    else:
        return answer