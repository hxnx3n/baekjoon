import sys
input = sys.stdin.readline

a = input().strip()
b = input().strip()

n, m = len(a), len(b)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

res = []
i, j = n, m
while i > 0 and j > 0:
    if a[i - 1] == b[j - 1]:
        res.append(a[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] >= dp[i][j - 1]:
        i -= 1
    else:
        j -= 1

print(''.join(reversed(res)))