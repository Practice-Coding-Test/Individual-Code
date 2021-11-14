import sys
n = int(sys.stdin.readline())
result = []
for i in range(0, n):
    tmp_list = list(map(int, sys.stdin.readline().split()))
    result_tmp_list = [0 for a in range(0, i + 1)]
    if i == 0:
        result_tmp_list = tmp_list
    for r in range(0, i):
        result_tmp = result[i-1][r]
        for j in range(0, i+1):
            if 2 > j-r > -1:
                tmp = result_tmp + tmp_list[j]
                if tmp > result_tmp_list[j]:
                    result_tmp_list[j] = tmp
    result.append(result_tmp_list)

print(max(result[-1]))
