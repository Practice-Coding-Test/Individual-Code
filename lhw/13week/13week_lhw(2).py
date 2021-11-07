#2
def function(k):
    check_list = list(k)
    check_set = set(k)
    if check_list == check_set:
        if len(check_list) == 10:
            Ans = True
    else:
        Ans = False
    return Ans
    
