def n_change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
def solution(n):
    three = str(n_change(n,3))
    answer = int(three[::-1],3)
    return answer
