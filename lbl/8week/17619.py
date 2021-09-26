import sys
N, Q = map(int,sys.stdin.readline().split())
L = []
for n in range(N):
    tmp = list(map(int,sys.stdin.readline().split()))
    tmp.append(n)  # 통나무 번호
    L.append(tmp)
L.sort(key=lambda x: (x[0]))
root = [i for i in range(N)]
def union(a,b):
    a_root = find(a)
    b_root = find(b)
    if a_root > b_root:
        root[a_root] = b_root
    else:
        root[b_root] = a_root
def find(x):
    if root[x] == x:
        return x
    else:
        root[x] = find(root[x])
        return root[x]
now = L[0]
for l in range(1,N):  # 연결되는 통나무 합치기
    if L[l][0] <= now[1]:
        now[1] = max(now[1],L[l][1])
        now[0] = min(now[0],L[l][0])
        union(L[l-1][3], L[l][3])  # 연결한 통나무 root 수정
    else:
        now = L[l]

for q in range(Q):
    start, end = map(int, sys.stdin.readline().split())
    start -= 1; end -= 1
    root[start] = find(start)
    root[end] = find(end)
    if root[start] == root[end]:
        print(1)
    else:
        print(0)
