import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[[0]*2 for _ in range(2*N+1)] for __ in range(N+1)]
INF = 10**18

def count(i, bal, wrong):
    if i == N:
        return 1 if wrong or bal != 0 else 0
    idx = bal+N
    if dp[i][idx][wrong]:
        return dp[i][idx][wrong]
    ret = 0
    ret += count(i+1, bal+1, wrong)
    ret += count(i+1, bal-1, wrong or bal <= 0)
    dp[i][idx][wrong] = min(ret, INF)
    return dp[i][idx][wrong]

total = count(0, 0, 0)
if K >= total:
    print(-1)
    sys.exit()

bal = 0
wrong = 0
res = []
for i in range(N):
    left_count = count(i+1, bal+1, wrong)
    if left_count > K:
        res.append("(")
        bal += 1
    else:
        res.append(")")
        K -= left_count
        wrong = wrong or bal <= 0
        bal -= 1
print("".join(res))
