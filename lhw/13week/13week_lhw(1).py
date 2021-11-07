#1
def function(n):
    fibolist = [0]*n
    fibolist[0] = 1
    fibolist[1] = 1
    for i in range(2,n):
        fibolist[i] = fibolist[i-1] + fibolist[i-2]
    return fibolist

#2
