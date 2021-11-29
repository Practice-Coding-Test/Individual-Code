def solution(tickets):
    answer = []
    answer.append("ICN")
    ch = [0]*len(tickets)
    tickets = sorted(tickets, key=lambda x: (x[0], x[1]))
    DFS("ICN", len(tickets), answer, ch, tickets)
    return answer

def DFS(start, cnt, answer, ch, tickets):
    if cnt == 0:
        return -1
    else:
        for i in range(len(tickets)):
            if start == tickets[i][0] and ch[i] == 0:
                answer.append(tickets[i][1])
                ch[i] = 1
                a = DFS(tickets[i][1], cnt-1, answer, ch, tickets)
                if(a != -1):
                    ch[i] = 0
                    answer.pop()
                else:
                    return -1
