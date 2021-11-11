def solution(s):
    try:
        if len(s) != 4 and len(s) != 6:
            return False
        s = int(s)
        return True
    except:
        return False