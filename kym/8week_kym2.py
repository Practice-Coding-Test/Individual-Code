import numpy as np
def solution(participant, completion):
    p = np.array(participant)
    c = np.array(completion)
    name = set(p) - set(c)
    if not name:
        unip, uni_cntp = np.unique(p,return_counts=True)
        unic, uni_cntc = np.unique(c,return_counts=True)
        tmp = uni_cntc == uni_cntp
        idx = np.where(tmp == False)
        return unip[idx][0]
    else:
        return ''.join(name)