import sys

T = int(sys.stdin.readline())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(T):
    M,N,K = map(int,sys.stdin.readline().split())
    ones = []
    for _ in range(0,K):
        X, Y = map(int,sys.stdin.readline().split())
        ones.append([X,Y])
    worm = 1
    visited = [ones.pop()]
    while ones:
        X, Y = visited.pop()
        for i in range(0,4):
            newX = X + dx[i]
            newY = Y + dy[i]
            if 0<=newX<M and 0<=newY<N and [newX, newY] in ones and [newX, newY] not in visited:
                ones.remove([newX,newY])
                visited.append([newX,newY])
        if len(visited) == 0:
            X, Y = ones.pop()
            worm += 1
            visited.append([X,Y])
    print(worm)
