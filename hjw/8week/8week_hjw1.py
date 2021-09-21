def solution(participant, completion):
    part = sorted(participant)
    com = sorted(completion)
    for i in range(len(part)):
        if part[i] != com[i]:
            return part[i]