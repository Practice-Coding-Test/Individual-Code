def solution(answers):
    c_1 = 0
    c_2 = 0
    c_3 = 0
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(0, len(answers)):
        if one[i % len(one)] == answers[i]:
            c_1 += 1
        if two[i % len(two)] == answers[i]:
            c_2 += 1
        if three[i % len(three)] == answers[i]:
            c_3 += 1

    return sorted([i + 1 for i, j in enumerate([c_1, c_2, c_3]) if j == max([c_1, c_2, c_3])])
