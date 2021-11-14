import sys

n = int(sys.stdin.readline())
dp = [0 for i in range(n)]
data = []
isLast = True
for i in range(0,n):
    data.append(int(sys.stdin.readline()))
for i in range(0,n):
    if i == 0:
        dp[0] = data[0]
    elif i == 1:
        dp[1] = dp[0] + data[1]
    elif i == 2:
        result = max(dp[0]+data[2],data[1]+data[2])
        dp[2] = max(result,dp[1])
    else:
        result = max(dp[i-2]+data[i],dp[i-3]+data[i-1]+data[i])
        dp[i] = max(result,dp[i-1])

print(dp[-1])
