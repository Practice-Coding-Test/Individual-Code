from itertools import combinations

def solution(orders, course):
    all_dict = {}
    answer = []

    for order in orders:
        for num in range(2, len(order)+1):
            result = list(combinations(order, num))
            for item in result:
                item = ''.join(sorted(item))
                if item in all_dict:
                    all_dict[item] += 1
                else:
                    all_dict[item] = 1

    for i in range(len(course)):
        c_max = 0
        for k, v in all_dict.items():
            if((len(k)==course[i]) and v>=2):
                c_max = max(c_max, v)

        for k, v in all_dict.items():
            if (v == c_max and len(k)==course[i]):
                answer.append(k)

    return sorted(answer)

