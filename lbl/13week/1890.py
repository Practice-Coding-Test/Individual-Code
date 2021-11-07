import sys

N = int(sys.stdin.readline())
data = []
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    data.append(tmp)
state = None
dp = [[0 for i in range(0,N)] for j in range(0,N)]
dp[0][0] = 1
for i in range(0,N):
    for j in range(0,N):
        if (dp[i][j] == 0 or (i == N-1 and j == N-1)):
            continue
        state = data[i][j]
        if i + state < N:
            dp[i+state][j] += dp[i][j]
        if j + state < N:
            dp[i][j+state] += dp[i][j]
print(dp[-1][-1])
