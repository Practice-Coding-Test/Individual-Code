def solution(participant, completion):
    import collections
    c = collections.Counter(sorted(participant)) - collections.Counter(sorted(completion))
    return list(c)[0]
