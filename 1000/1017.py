import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

MAX = 2000
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in range(2, int(MAX**0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX+1, i):
            prime[j] = False

first = A[0]
rest = A[1:]

if first % 2 == 0:
    L = [x for x in rest if x % 2 == 1]
    R = [x for x in rest if x % 2 == 0]
else:
    L = [x for x in rest if x % 2 == 0]
    R = [x for x in rest if x % 2 == 1]

ans = []

for cand in L:
    if not prime[first + cand]:
        continue

    matchR = [-1] * len(R)

    def dfs(li, visited):
        for ri in range(len(R)):
            if prime[L[li] + R[ri]] and not visited[ri]:
                visited[ri] = True
                if matchR[ri] == -1 or dfs(matchR[ri], visited):
                    matchR[ri] = li
                    return True
        return False

    ok = True
    for i in range(len(L)):
        if L[i] == cand:
            continue
        visited = [False] * len(R)
        if not dfs(i, visited):
            ok = False
            break

    if ok:
        ans.append(cand)

ans.sort()
if ans:
    print(*ans)
else:
    print(-1)
